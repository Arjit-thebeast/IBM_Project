import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.blank("en")
ruler = nlp.add_pipe("entity_ruler")

# Skill patterns matching canonical skills across data science, web development, cloud & databases
patterns = [
    # Data Science & AI
    {"label": "SKILL", "pattern": [{"LOWER": "python"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "machine"}, {"LOWER": "learning"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "deep"}, {"LOWER": "learning"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "artificial"}, {"LOWER": "intelligence"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "data"}, {"LOWER": "science"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "data"}, {"LOWER": "analysis"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "data"}, {"LOWER": "analytics"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "statistical"}, {"LOWER": "modeling"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "predictive"}, {"LOWER": "modeling"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "nlp"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "natural"}, {"LOWER": "language"}, {"LOWER": "processing"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "computer"}, {"LOWER": "vision"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "rag"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "langchain"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "statistics"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "mathematics"}]},

    # Databases & Big Data
    {"label": "SKILL", "pattern": [{"LOWER": "sql"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "mysql"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "postgresql"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "big"}, {"LOWER": "data"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "spark"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "pyspark"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "hadoop"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "cassandra"}]},

    # Business Intelligence & Visualization
    {"label": "SKILL", "pattern": [{"LOWER": "power"}, {"LOWER": "bi"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "tableau"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "excel"}]},

    # Cloud & Infrastructure
    {"label": "SKILL", "pattern": [{"LOWER": "aws"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "azure"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "gcp"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "cloud"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "docker"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "kubernetes"}]},

    # Programming Languages & Web
    {"label": "SKILL", "pattern": [{"LOWER": "java"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "c++"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "scala"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "html"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "css"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "javascript"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "react"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "node.js"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "git"}]},

    # Python Data Ecosystem
    {"label": "SKILL", "pattern": [{"LOWER": "pandas"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "numpy"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "scikit-learn"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "sklearn"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "tensorflow"}]},
    {"label": "SKILL", "pattern": [{"LOWER": "pytorch"}]},
]

ruler.add_patterns(patterns)

SKILL_NAME_MAP = {
    "python": "Python",
    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "artificial intelligence": "Artificial Intelligence",
    "data science": "Data Science",
    "data analysis": "Data Analysis",
    "data analytics": "Data Analysis",
    "statistical modeling": "Statistical Modeling",
    "predictive modeling": "Predictive Modeling",
    "nlp": "NLP",
    "natural language processing": "NLP",
    "computer vision": "Computer Vision",
    "rag": "RAG",
    "langchain": "LangChain",
    "statistics": "Statistics",
    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "big data": "Big Data",
    "spark": "Apache Spark",
    "pyspark": "PySpark",
    "hadoop": "Hadoop",
    "cassandra": "Cassandra",
    "power bi": "Power BI",
    "tableau": "Tableau",
    "excel": "Excel",
    "aws": "AWS",
    "azure": "Azure",
    "gcp": "GCP",
    "cloud": "Cloud Computing",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "java": "Java",
    "c++": "C++",
    "scala": "Scala",
    "html": "HTML",
    "css": "CSS",
    "javascript": "JavaScript",
    "react": "React",
    "node.js": "Node.js",
    "git": "Git",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "scikit-learn": "Scikit-Learn",
    "sklearn": "Scikit-Learn",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
}


def extract_skills(text):
    """
    Extract technical skills from text using spaCy entity ruler and normalize display names.
    """
    doc = nlp(text)
    extracted = []

    for ent in doc.ents:
        if ent.label_ == "SKILL":
            val_lower = ent.text.lower()
            canonical_name = SKILL_NAME_MAP.get(val_lower, ent.text.title())
            extracted.append(canonical_name)

    # Deduplicate while preserving order
    unique_skills = []
    for s in extracted:
        if s not in unique_skills:
            unique_skills.append(s)

    return unique_skills