import streamlit as st
import pandas as pd
import time
from scraper import scrape_wuzzuf
from data_cleaning import clean_data, validate_uploaded_data
from visualizations import *

# Page configuration
st.set_page_config(
    page_title="Wuzzuf Jobs Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #3B82F6;
        margin-bottom: 2rem;
        text-align: center;
    }
    .info-box {
        background-color: #F0F8FF;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 1rem;
    }
    .warning-box {
        background-color: #FFF3CD;
        padding: 1rem;
        border-radius: 5px;
        border-left: 3px solid #FFC107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #D4EDDA;
        padding: 1rem;
        border-radius: 5px;
        border-left: 3px solid #28A745;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📊 Wuzzuf Jobs Data Analysis Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Explore Data Jobs Market in Egypt and Beyond</p>', unsafe_allow_html=True)

# Sidebar for data source selection
with st.sidebar:
    st.image("https://wuzzuf.net/images/logo.png", width=200)
    st.markdown("## ⚙️ Data Source")
    
    data_option = st.radio(
        "Choose how to load data:",
        [
            "📁 Use existing CSV (Wuzzuf.csv)",
            "🆕 Scrape fresh data from Wuzzuf",
            "📤 Upload your own CSV file"
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("## 📊 Dashboard Info")
    st.markdown("This dashboard analyzes job postings from Wuzzuf.net")
    st.markdown("- **Total Jobs:** Will appear after loading")
    
    st.markdown("---")
    st.markdown("### 📌 Quick Tips")
    st.markdown("• Hover over charts for details")
    st.markdown("• Use double-click to zoom")
    st.markdown("• Download raw data below")

# Main content area
df = None
data_loaded = False

# Load data based on selection
if data_option == "📁 Use existing CSV (Wuzzuf.csv)":
    try:
        df = pd.read_csv("Wuzzuf.csv")
        st.sidebar.success("✅ Loaded existing CSV")
        data_loaded = True
    except FileNotFoundError:
        st.sidebar.error("❌ Wuzzuf.csv not found. Please scrape data or upload a file.")
        st.info("👈 Please choose another option from the sidebar to load data.")

elif data_option == "🆕 Scrape fresh data from Wuzzuf":
    st.sidebar.warning("⚠️ This will take about 2-3 minutes")
    if st.sidebar.button("🚀 Start Scraping"):
        # Create progress bar
        progress_bar = st.progress(0, text="Starting scraping...")
        status_text = st.empty()
        
        # Define progress callback
        def update_progress(current, total, message):
            progress = (current + 1) / total
            progress_bar.progress(progress)
            status_text.text(message)
        
        try:
            with st.spinner("Scraping data from Wuzzuf..."):
                # Pass the callback function
                df = scrape_wuzzuf(pages=41, progress_callback=update_progress)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                if len(df) > 0:
                    # Save to CSV file
                    df.to_csv("Wuzzuf.csv", index=False)
                    
                    # Show success message
                    st.sidebar.success(f"✅ Scraping complete! Found {len(df)} jobs")
                    
                    # Load the data directly without rerun
                    data_loaded = True
                    
                else:
                    st.error("No data was scraped. Please try again.")
                    
        except Exception as e:
            st.error(f"Error during scraping: {e}")
            progress_bar.empty()
            status_text.empty()

elif data_option == "📤 Upload your own CSV file":
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Validate the uploaded data
        is_valid, message = validate_uploaded_data(df)
        
        if is_valid:
            st.sidebar.success(message)
            data_loaded = True
        else:
            # Show warning with required columns
            st.sidebar.error(message)
            
            # Show detailed requirements in an expander
            with st.sidebar.expander("📋 Required Columns Format"):
                st.markdown("""
                <div class="warning-box">
                <strong>Your CSV must have these columns:</strong><br>
                • <code>job_title</code> - Job position title<br>
                • <code>companies</code> - Company names<br>
                • <code>locations</code> - Full location (e.g., "Cairo, Egypt")<br>
                • <code>employment_types</code> - Full Time, Internship, etc.<br>
                • <code>work_modes</code> - On-site, Remote, Hybrid<br>
                • <code>skills</code> - Skills required for the job<br><br>
                
                <strong>Example row:</strong><br>
                <code>Data Analyst,Google,"Cairo, Egypt",Full Time,On-site,"Python, SQL"</code>
                </div>
                """, unsafe_allow_html=True)
                
                # Show sample dataframe structure
                sample_df = pd.DataFrame({
                    'job_title': ['Data Analyst'],
                    'companies': ['Google'],
                    'locations': ['Cairo, Egypt'],
                    'employment_types': ['Full Time'],
                    'work_modes': ['On-site'],
                    'skills': ['Python, SQL']
                })
                st.dataframe(sample_df)

# If data is loaded, show visualizations
if data_loaded and df is not None:
    
    # Clean the data
    with st.spinner("Cleaning and processing data..."):
        df = clean_data(df)
    
    # Display key metrics
    st.markdown("## 📈 Key Metrics")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Jobs", len(df))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Unique Companies", df['companies'].nunique())
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Cities", df['city'].nunique())
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Countries", df['country'].nunique())
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col5:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        remote_pct = (df['work_modes'] == 'Remote').mean() * 100
        st.metric("Remote Jobs", f"{remote_pct:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Job Distribution", "🌍 Geographic Analysis", "🏢 Employment Details", "🔧 Skills Analysis"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(top5_jobs(df), use_container_width=True)
        
        with col2:
            st.plotly_chart(work_mode_pie(df), use_container_width=True)
        
        # Employment types chart
        st.plotly_chart(employment_types_chart(df), use_container_width=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(jobs_per_city(df), use_container_width=True)
        
        with col2:
            st.plotly_chart(jobs_per_country_line(df), use_container_width=True)
        
        # World map
        st.plotly_chart(choropleth_map(df), use_container_width=True)
        
        # Remote jobs by city
        st.plotly_chart(remote_jobs_city(df), use_container_width=True)
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            # Employment types pie chart
            emp_types = df['employment_types'].value_counts().reset_index()
            emp_types.columns = ['type', 'count']
            fig_emp = px.pie(emp_types, values='count', names='type', 
                           title="Employment Types Distribution",
                           color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(fig_emp, use_container_width=True)
        
        with col2:
            # Companies with most jobs
            top_companies = df['companies'].value_counts().head(10).reset_index()
            top_companies.columns = ['company', 'count']
            fig_comp = px.bar(top_companies, x='count', y='company', 
                            orientation='h', title="Top 10 Companies Hiring",
                            color='count', color_continuous_scale='Blues')
            st.plotly_chart(fig_comp, use_container_width=True)
    
    with tab4:
        # Skills analysis
        st.plotly_chart(skills_wordcloud(df), use_container_width=True)
        
        # Show top skills in table
        all_skills = df['skills'].dropna().str.cat(sep=' ')
        skill_list = all_skills.split()
        skill_freq = pd.Series(skill_list).value_counts().head(20).reset_index()
        skill_freq.columns = ['Skill', 'Frequency']
        
    #    st.markdown("### 🔝 Top 20 Skills")
    #    st.dataframe(skill_freq, use_container_width=True)
    
    st.markdown("---")
    
    # Raw data section
    with st.expander("📋 View Raw Data"):
        st.dataframe(df, use_container_width=True)
        
        # Download buttons
        col1, col2 = st.columns(2)
        with col1:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Cleaned Data (CSV)",
                data=csv,
                file_name="Wuzzuf_cleaned.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col2:
            # Summary statistics download
            summary = df.describe(include='all').to_csv()
            st.download_button(
                label="📥 Download Summary Statistics",
                data=summary,
                file_name="Wuzzuf_summary.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray; padding: 1rem;'>"
        "Dashboard created with ❤️ using Streamlit | Data sourced from Wuzzuf.net"
        "</div>", 
        unsafe_allow_html=True
    )

else:
    # Show welcome message when no data is loaded
    st.markdown("""
    <div style='text-align: center; padding: 3rem;'>
        <h2>👋 Welcome to the Wuzzuf Jobs Dashboard!</h2>
        <p style='font-size: 1.2rem; color: gray;'>Please select a data source from the sidebar to get started.</p>
    </div>
    """, unsafe_allow_html=True)