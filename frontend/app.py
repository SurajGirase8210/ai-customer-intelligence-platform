import streamlit as st


st.set_page_config(
    page_title="Customer Intelligence Copilot",
    page_icon="📊",
    layout="wide"
)


st.title("AI Customer Intelligence and Retention Platform")

st.markdown(
    """
    ### Understand customers. Predict churn. Recommend actions.
    
    This platform will combine:
    - Predictive Machine Learning
    - Customer segmentation and analytics
    - Generative AI with retrieval-augmented generation (RAG)
    """
)


st.info(
    "Project setup is complete."
    "Customer analytics and prediction features are coming next."
)

st.subheader("Planned capabilities")

col1, col2, col3 = st.columns(3)

col1.metric("ML models", "In development")
col2.metric("Customer Segmentation", "In development")
col3.metric("AI Copilot", "In development")