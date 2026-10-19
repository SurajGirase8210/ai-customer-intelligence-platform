from fastapi import FastAPI

app = FastAPI(
    title="AI CUSTOMER INTELLIGENCE AND RETENTION COPILOT",
    description=(
        "Machine Learning and Generative AI"
        "for customer churn analysis and retention"
    ),
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        'project': 'AI CUSTOMER INTELLIGENCE AND RETENTION COPILOT',
        'status': 'running',
        'version': '0.1.0'
    }
    
@app.get("/health")
def health_check():
    return {
        'status': 'healthy',
        'service':'customer intelligence api'
    }
    
    