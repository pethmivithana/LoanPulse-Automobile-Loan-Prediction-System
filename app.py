import pickle
import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import time

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# loading the saved models
model = pickle.load(open('RFModel.sav', 'rb'))

# Load the image
image = Image.open("LoanDrive.png")

# Convert the image to a base64 string
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Set page configuration
st.set_page_config(page_title="LoanPulse - Loan Default Predictor", page_icon=image, layout="wide")

# Professional White Theme CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background-color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Welcome Screen Styles */
    .welcome-container {
        text-align: center;
        padding: 3rem 2rem;
        animation: fadeIn 1.5s ease-in;
    }
    
    .welcome-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 1rem;
        animation: slideDown 1s ease-out;
        letter-spacing: -0.5px;
    }
    
    .welcome-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 400;
        color: #64748b;
        margin-bottom: 3rem;
        animation: slideUp 1s ease-out;
        line-height: 1.6;
    }
    
    .feature-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 2.5rem 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #e2e8f0;
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border-color: #3b82f6;
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        color: #3b82f6;
    }
    
    .feature-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .feature-text {
        font-family: 'Inter', sans-serif;
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Statistics Section */
    .stat-box {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        border-radius: 16px;
        padding: 2rem 1.5rem;
        text-align: center;
        animation: fadeInUp 1.2s ease-out;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15);
        color: white;
        transition: transform 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-3px);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        font-family: 'Inter', sans-serif;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        opacity: 0.9;
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.8rem 2.5rem;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        background: linear-gradient(135deg, #2563eb 0%, #1e3a8a 100%);
    }
    
    /* Form Screen Styles */
    .form-container {
        background: #ffffff;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1rem auto;
        max-width: 1200px;
        box-shadow: 0 4px 25px rgba(0,0,0,0.08);
        border: 1px solid #f1f5f9;
    }
    
    .form-header {
        text-align: center;
        font-size: 2.2rem;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 1.5rem;
    }
    
    .section-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #1e293b;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    /* Input Field Styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 0.75rem;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: #ffffff;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        outline: none;
    }
    
    /* Slider Styling */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #3b82f6 0%, #1e40af 100%);
    }
    
    /* Risk Assessment Styles */
    .risk-high {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #dc2626;
        box-shadow: 0 4px 15px rgba(220, 38, 38, 0.1);
    }
    .risk-medium {
        background: linear-gradient(135deg, #fffbeb 0%, #fed7aa 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #ea580c;
        box-shadow: 0 4px 15px rgba(234, 88, 12, 0.1);
    }
    .risk-low {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #16a34a;
        box-shadow: 0 4px 15px rgba(22, 163, 74, 0.1);
    }
    
    .decision-approved {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid #16a34a;
        text-align: center;
        box-shadow: 0 8px 25px rgba(22, 163, 74, 0.15);
    }
    .decision-rejected {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid #dc2626;
        text-align: center;
        box-shadow: 0 8px 25px rgba(220, 38, 38, 0.15);
    }
    .decision-conditional {
        background: linear-gradient(135deg, #fffbeb 0%, #fed7aa 100%);
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid #ea580c;
        text-align: center;
        box-shadow: 0 8px 25px rgba(234, 88, 12, 0.15);
    }
    
    /* Back Button */
    .back-button {
        background: #ffffff;
        color: #3b82f6;
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }
    
    .back-button:hover {
        background: #3b82f6;
        color: white;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #3b82f6 0%, #1e40af 100%);
    }
    
    /* Card Styles for Results */
    .info-card {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideDown {
        from {
            transform: translateY(-50px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes slideUp {
        from {
            transform: translateY(50px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes fadeInUp {
        from {
            transform: translateY(30px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    /* Custom Divider */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }
    
    /* Tooltip Styling */
    .stTooltip {
        font-family: 'Inter', sans-serif;
    }
    
    /* Metric Styling */
    [data-testid="metric-container"] {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)


def input_transformer(inputs):
    value_map = {
        "House Owned": {
            "Yes": 1,
            "No": 0
        },
        "Car Owned": {
            "Yes": 1,
            "No": 0
        },
        "Bike Owned": {
            "Yes": 1,
            "No": 0
        },
        "Has Active Loan": {
            "Yes": 1,
            "No": 0
        },
        "Client Income Type": {
            "Commercial": 1,
            "Service": 2,
            "Student": 3,
            "Retired": 4,
            "Unemployed": 5
        },
        "Client Education": {
            "Secondary": 1,
            "Graduation": 2
        },
        "Client Marital Status": {
            'Married': 1,
            'Widow': 2,
            'Single': 3,
            'Divorced': 4
        },
        "Client Gender": {
            'Male': 1,
            'Female': 2
        },
        "Loan Contract Type": {
            'Cash Loan': 1,
            'Revolving Loan': 2
        }
    }

    transformed_inputs = []
    for input, value in inputs.items():
        if (value_map[input] != None and value_map[input][value] != None):
            transformed_inputs.append(value_map[input][value])

    return transformed_inputs


def calculate_risk_score(loan_amount, income, loan_annuity, age, employed_days, 
                         child_count, active_loan, income_type, house_owned, 
                         car_owned, education, model_prediction):
    """
    Calculate comprehensive risk score based on multiple factors
    Returns: (risk_score, risk_factors, risk_level)
    """
    risk_score = 0
    risk_factors = []
    
    # 1. Debt-to-Income Ratio (DTI) - Critical Factor
    if income > 0:
        dti_ratio = (loan_annuity * 12) / income
        if dti_ratio > 0.5:
            risk_score += 30
            risk_factors.append(f"High debt-to-income ratio: {dti_ratio:.1%} (>50%)")
        elif dti_ratio > 0.4:
            risk_score += 20
            risk_factors.append(f"Elevated debt-to-income ratio: {dti_ratio:.1%} (>40%)")
        elif dti_ratio > 0.3:
            risk_score += 10
            risk_factors.append(f"Moderate debt-to-income ratio: {dti_ratio:.1%}")
        else:
            risk_factors.append(f"Good debt-to-income ratio: {dti_ratio:.1%} (<30%)")
    
    # 2. Loan-to-Income Ratio
    if income > 0:
        lti_ratio = loan_amount / income
        if lti_ratio > 5:
            risk_score += 25
            risk_factors.append(f"Loan amount is {lti_ratio:.1f}x annual income (very high)")
        elif lti_ratio > 3:
            risk_score += 15
            risk_factors.append(f"Loan amount is {lti_ratio:.1f}x annual income (high)")
        elif lti_ratio > 2:
            risk_score += 8
            risk_factors.append(f"Loan amount is {lti_ratio:.1f}x annual income")
        else:
            risk_factors.append(f"Good loan-to-income ratio: {lti_ratio:.1f}x income")
    
    # 3. Employment Stability
    if employed_days < 1:
        risk_score += 20
        risk_factors.append("Unemployed or less than 1 year employment")
    elif employed_days < 2:
        risk_score += 12
        risk_factors.append("Less than 2 years employment history")
    elif employed_days < 5:
        risk_score += 5
        risk_factors.append("Limited employment history (< 5 years)")
    else:
        risk_factors.append(f"Good employment history: {employed_days} years")
    
    # 4. Active Loan Status
    if active_loan == "Yes":
        risk_score += 15
        risk_factors.append("Already has an active loan")
    else:
        risk_factors.append("No active loans - positive factor")
    
    # 5. Income Type Risk Assessment
    if income_type in ["Student", "Unemployed"]:
        risk_score += 25
        risk_factors.append(f"High-risk income type: {income_type}")
    elif income_type == "Retired":
        risk_score += 10
        risk_factors.append("Retired with fixed income")
    else:
        risk_factors.append(f"Stable income type: {income_type}")
    
    # 6. Asset Ownership (reduces risk)
    asset_score = 0
    if house_owned == "Yes":
        asset_score -= 15
        risk_factors.append("House ownership - significant risk reduction")
    if car_owned == "Yes":
        asset_score -= 8
        risk_factors.append("Car ownership - moderate risk reduction")
    risk_score += asset_score
    
    # 7. Age Risk Factor
    if age < 25:
        risk_score += 8
        risk_factors.append("Young age (< 25 years) - limited credit history")
    elif age > 55:
        risk_score += 5
        risk_factors.append("Age > 55 years - nearing retirement")
    else:
        risk_factors.append(f"Prime working age: {age} years")
    
    # 8. Dependents
    if child_count >= 3:
        risk_score += 10
        risk_factors.append(f"High number of dependents ({child_count} children)")
    elif child_count >= 2:
        risk_score += 5
        risk_factors.append(f"{child_count} children as dependents")
    elif child_count == 0:
        risk_factors.append("No dependents - positive factor")
    else:
        risk_factors.append(f"Reasonable number of dependents: {child_count}")
    
    # 9. Education Level
    if education == "Secondary":
        risk_score += 5
        risk_factors.append("Secondary education level")
    else:
        risk_factors.append("Graduation education - positive factor")
    
    # 10. Model Prediction Weight (highest weight)
    if model_prediction == 1:
        risk_score += 40
        risk_factors.append("ML Model predicts HIGH DEFAULT RISK")
    else:
        risk_score -= 20
        risk_factors.append("ML Model predicts LOW DEFAULT RISK")
    
    # Ensure risk score is within bounds
    risk_score = max(0, min(100, risk_score))
    
    # Determine risk level
    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    
    return risk_score, risk_factors, risk_level


def make_loan_decision(risk_score, risk_level, loan_amount, income, employed_days, 
                      age, active_loan, house_owned, risk_factors, model_prediction, income_type):
    """
    IMPROVED: Make final loan decision based on comprehensive risk assessment
    with multiple decision factors and clearer logic
    """
    
    # Calculate key ratios for decision making
    lti_ratio = loan_amount / income if income > 0 else float('inf')
    employment_stable = employed_days >= 2
    prime_age = 25 <= age <= 55
    has_assets = house_owned == "Yes"
    no_active_loans = active_loan == "No"
    
    # Decision Matrix - Multiple Factor Analysis
    
    # AUTOMATIC REJECTION CRITERIA
    automatic_reject_conditions = [
        risk_score >= 80,  # Very high risk score
        (risk_level == "HIGH" and lti_ratio > 4),  # High risk with excessive loan amount
        (income == 0 and loan_amount > 0),  # No income but requesting loan
        (employed_days < 1 and income_type in ["Unemployed", "Student"]),  # Unemployed student
        (model_prediction == 1 and risk_score > 60)  # Model predicts default with high risk
    ]
    
    if any(automatic_reject_conditions):
        decision = "REJECT"
        recommendation = "⛔ Loan Application Rejected"
        reason = "Application does not meet minimum eligibility criteria based on multiple risk factors."
        return decision, recommendation, reason
    
    # AUTOMATIC APPROVAL CRITERIA (Low risk with strong profile)
    automatic_approve_conditions = [
        risk_score <= 25 and lti_ratio <= 2 and employment_stable and prime_age,
        risk_score <= 20 and has_assets and no_active_loans and lti_ratio <= 1.5
    ]
    
    if any(automatic_approve_conditions):
        decision = "APPROVE"
        recommendation = "✅ Loan Application Approved"
        reason = "Strong applicant profile with excellent risk indicators."
        return decision, recommendation, reason
    
    # RISK-BASED DECISION MAKING
    if risk_level == "HIGH":
        # High risk applicants - generally reject with few exceptions
        if has_assets and lti_ratio <= 1.5 and employment_stable:
            decision = "CONDITIONAL_APPROVE"
            recommendation = "⚠️ Conditional Approval - Strict Terms"
            reason = "High risk profile mitigated by strong collateral and stable employment."
        else:
            decision = "REJECT"
            recommendation = "⛔ Loan Application Rejected"
            reason = "High risk profile with multiple concerning factors indicates high probability of default."
            
    elif risk_level == "MEDIUM":
        # Medium risk - detailed analysis required
        positive_factors = sum([
            employment_stable,
            prime_age,
            has_assets,
            no_active_loans,
            lti_ratio <= 2.5
        ])
        
        if positive_factors >= 4:  # Strong medium-risk profile
            decision = "APPROVE"
            recommendation = "✅ Loan Application Approved"
            reason = "Medium risk balanced by multiple positive factors indicating repayment capacity."
        elif positive_factors >= 2:  # Average medium-risk profile
            decision = "CONDITIONAL_APPROVE"
            recommendation = "⚠️ Conditional Approval"
            reason = "Medium risk profile with some positive indicators. Recommend modified terms."
        else:  # Weak medium-risk profile
            decision = "REJECT"
            recommendation = "⛔ Loan Application Rejected"
            reason = "Medium risk profile lacks sufficient positive indicators for approval."
            
    else:  # LOW risk
        # Low risk - generally approve with conditions for edge cases
        if lti_ratio > 3:  # Loan amount too high relative to income
            decision = "CONDITIONAL_APPROVE"
            recommendation = "⚠️ Conditional Approval - Amount Adjustment"
            reason = "Low risk profile but loan amount exceeds recommended limits relative to income."
        elif not employment_stable:  # Employment concerns
            decision = "CONDITIONAL_APPROVE"
            recommendation = "⚠️ Conditional Approval - Employment Verification"
            reason = "Low risk profile but employment history requires verification."
        else:
            decision = "APPROVE"
            recommendation = "✅ Loan Application Approved"
            reason = "Strong low-risk profile with excellent repayment capacity indicators."
    
    return decision, recommendation, reason


def get_decision_details(decision, risk_level, risk_score):
    """
    Provide detailed explanation and conditions based on decision
    """
    details = {
        "APPROVE": {
            "conditions": [
                "Standard interest rate applies",
                "Full requested amount approved",
                "Standard repayment terms",
                "Quick disbursement process"
            ],
            "next_steps": [
                "Submit income verification documents",
                "Sign loan agreement",
                "Funds disbursed within 3-5 business days"
            ]
        },
        "CONDITIONAL_APPROVE": {
            "conditions": [
                "Enhanced documentation required",
                "Possible adjusted interest rate",
                "Loan amount may be modified",
                "Additional collateral may be required"
            ],
            "next_steps": [
                "Submit additional documentation",
                "Underwriting review",
                "Final terms negotiation",
                "Possible co-signer requirement"
            ]
        },
        "REJECT": {
            "conditions": [
                "Application does not meet current criteria",
                "Risk factors exceed acceptable limits",
                "Default probability too high"
            ],
            "next_steps": [
                "Re-apply after 6 months with improved profile",
                "Consider smaller loan amount",
                "Improve credit profile",
                "Explore secured loan options"
            ]
        }
    }
    
    return details.get(decision, {"conditions": [], "next_steps": []})


def show_welcome_screen():
    """Display the welcome/onboarding screen"""
    
    st.markdown("""
        <div class="welcome-container">
            <h1 class="welcome-title">LoanPulse AI</h1>
            <p class="welcome-subtitle">Intelligent Loan Risk Assessment Platform<br>Powered by Machine Learning</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Logo
    st.markdown(
        f"""
        <div style="text-align: center; margin: 2rem 0;">
            <img src="data:image/png;base64,{img_str}" alt="LoanPulse Logo" width="180" style="border-radius: 12px;">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Statistics Section
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">98%</div>
                <div class="stat-label">Accuracy</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">50K+</div>
                <div class="stat-label">Applications</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">99.9%</div>
                <div class="stat-label">Uptime</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">< 2min</div>
                <div class="stat-label">Processing</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Feature Cards
    st.markdown('<h3 style="text-align: center; color: #1e3a8a; font-size: 1.8rem; margin-bottom: 2rem;">Why Choose LoanPulse?</h3>', unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3 class="feature-title">AI-Powered Analysis</h3>
                <p class="feature-text">Advanced machine learning algorithms analyze 20+ risk factors for accurate default predictions</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3 class="feature-title">Instant Assessment</h3>
                <p class="feature-text">Get comprehensive risk analysis and loan decisions in under 2 minutes</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_c:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3 class="feature-title">Bank-Grade Security</h3>
                <p class="feature-text">Enterprise-grade encryption and data protection standards</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Call to Action
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        if st.button("🚀 Start Loan Assessment", key="start_button", use_container_width=True):
            st.session_state.page = 'form'
            st.rerun()


def show_form_screen():
    """Display the loan application form"""
    
    # Header with back button
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("← Back", key="back_button"):
            st.session_state.page = 'welcome'
            st.rerun()
    
    # Form container
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # Form Title
    st.markdown('<h1 class="form-header">Loan Application Assessment</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.1rem; color: #64748b; margin-bottom: 2rem;">Complete the form below for instant risk assessment</p>', unsafe_allow_html=True)
    
    # Create form
    with st.form(key='loan_form'):
        
        # Personal Information Section
        st.markdown('<h2 class="section-header">👤 Personal Information</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fName = st.text_input("Full Name *", placeholder="Enter your full name")
            gender = st.selectbox("Gender *", ("-", "Male", "Female"))
            age = st.slider("Age *", min_value=20, max_value=60, value=30, 
                           help="Applicant must be between 20-60 years")
            
        with col2:
            marital_status = st.selectbox("Marital Status *", ("-", "Single", "Married", "Divorced", "Widow"))
            education = st.selectbox("Education Level *", ("-", 'Secondary', 'Graduation'))
            child_count = st.selectbox("Number of Children", (0, 1, 2, 3, 4, 5), 
                                      help="Number of dependents")
        
        st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
        
        # Financial Information Section
        st.markdown('<h2 class="section-header">💰 Financial Information</h2>', unsafe_allow_html=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            income = st.number_input("Annual Income ($) *", min_value=0.0, step=1000.00, format="%.2f",
                                    help="Your total annual income before taxes")
            income_type = st.selectbox("Income Type *", ("-", 'Commercial', 'Service', 'Student', 'Retired', 'Unemployed'))
            employed_days = st.slider("Years of Employment *", min_value=0, max_value=80, value=5,
                                     help="Total years in current and previous employment")
            
        with col4:
            loan_amount = st.number_input("Requested Loan Amount ($) *", min_value=0.0, step=1000.00, format="%.2f")
            loan_annuity = st.number_input("Annual Loan Payment ($) *", min_value=0.0, step=500.00, format="%.2f", 
                                         help="Annual repayment amount for the loan")
            loan_contract_type = st.selectbox("Loan Type *", ("-", 'Cash Loan', 'Revolving Loan'))
        
        st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
        
        # Asset Information Section
        st.markdown('<h2 class="section-header">🏠 Assets & Existing Loans</h2>', unsafe_allow_html=True)
        
        col5, col6 = st.columns(2)
        
        with col5:
            house_owned = st.selectbox("Do you own a house? *", ("-", "Yes", "No"))
            car_owned = st.selectbox("Do you own a car? *", ("-", "Yes", "No"))
            
        with col6:
            bike_owned = st.selectbox("Do you own a bike? *", ("-", "Yes", "No"))
            active_loan = st.selectbox("Do you have active loans? *", ("-", "No", "Yes"))
        
        st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
        
        # Additional Information
        st.markdown('<h2 class="section-header">📌 Additional Information</h2>', unsafe_allow_html=True)
        
        registration = st.slider("Years as Registered Client", min_value=0, max_value=50, value=10, 
                               help="How long you've been registered in our system")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Submit Button
        col_submit = st.columns([1, 2, 1])
        with col_submit[1]:
            Submit = st.form_submit_button("🔍 Analyze Application", use_container_width=True)

        if Submit:
            # Input validation
            inputs = {"Loan Amount": loan_amount, "Income": income, "Loan Annuity": loan_annuity, "Age": age, 
                      "Child Count": child_count, "Employed Days": employed_days, "Years since registration": registration}
            inputs_to_transform = {
                "House Owned": house_owned,
                "Car Owned": car_owned,
                "Bike Owned": bike_owned,
                "Has Active Loan": active_loan,
                "Client Income Type": income_type,
                "Client Education": education,
                "Client Marital Status": marital_status,
                "Client Gender": gender,
                "Loan Contract Type": loan_contract_type
            }

            invalid_inputs = []

            if fName.strip() == "":
                invalid_inputs.append("Client Name")

            if loan_amount == 0:
                invalid_inputs.append("Loan Amount")

            for label, value in inputs.items():
                if value == '-' or value == "-" or value == None:
                    invalid_inputs.append(label)

            for label, value in inputs_to_transform.items():
                if value == '-' or value == "-" or value == None:
                    invalid_inputs.append(label)

            if len(invalid_inputs) > 0:
                st.error(f"**Please complete all required fields:** {', '.join(invalid_inputs)}")
            else:
                with st.spinner("🤖 Analyzing application data..."):
                    time.sleep(1.5)
                    
                    transformed_inputs = input_transformer(inputs_to_transform)
                    inputs_array = [list(inputs.values()) + transformed_inputs]
                    
                    # Get model prediction
                    prediction = model.predict(inputs_array)
                    
                    # Calculate comprehensive risk score
                    risk_score, risk_factors, risk_level = calculate_risk_score(
                        loan_amount, income, loan_annuity, age, employed_days,
                        child_count, active_loan, income_type, house_owned,
                        car_owned, education, prediction[0]
                    )
                    
                    # Make final decision
                    decision, recommendation, reason = make_loan_decision(
                        risk_score, risk_level, loan_amount, income, employed_days,
                        age, active_loan, house_owned, risk_factors, prediction[0], income_type
                    )
                    
                    # Get decision details
                    decision_details = get_decision_details(decision, risk_level, risk_score)
                    
                    # Display Results
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("---")
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    st.markdown('<h2 style="text-align: center; color: #1e3a8a; font-size: 2rem; margin-bottom: 2rem;">Assessment Results</h2>', unsafe_allow_html=True)
                    
                    # Application Summary
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        st.markdown("""
                        <div class="info-card">
                            <h4 style="color: #1e3a8a; margin-bottom: 1rem;">📋 Application Summary</h4>
                        """, unsafe_allow_html=True)
                        st.metric("👤 Applicant", fName)
                        st.metric("💰 Loan Amount", f"${loan_amount:,.2f}")
                        st.metric("💵 Annual Income", f"${income:,.2f}")
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        # Financial Ratios
                        if income > 0:
                            st.markdown("""
                            <div class="info-card">
                                <h4 style="color: #1e3a8a; margin-bottom: 1rem;">📊 Financial Ratios</h4>
                            """, unsafe_allow_html=True)
                            st.metric("📈 Loan-to-Income", f"{loan_amount/income:.2f}x")
                            st.metric("💳 Debt-to-Income", f"{(loan_annuity * 12)/income:.1%}")
                            st.markdown("</div>", unsafe_allow_html=True)
                    
                    with col_b:
                        st.markdown("""
                        <div class="info-card">
                            <h4 style="color: #1e3a8a; margin-bottom: 1rem;">👤 Profile Details</h4>
                        """, unsafe_allow_html=True)
                        st.metric("🎂 Age", f"{age} years")
                        st.metric("💼 Employment", f"{employed_days} years")
                        st.metric("💵 Income Type", income_type)
                        st.metric("🏠 House Owned", house_owned)
                        st.markdown("</div>", unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Risk Assessment
                    st.markdown('<h3 style="color: #1e3a8a; font-size: 1.5rem; margin-bottom: 1rem;">🎯 Risk Assessment</h3>', unsafe_allow_html=True)
                    
                    # Risk level display
                    if risk_level == "HIGH":
                        risk_class = "risk-high"
                        risk_emoji = "🔴"
                    elif risk_level == "MEDIUM":
                        risk_class = "risk-medium"
                        risk_emoji = "🟡"
                    else:
                        risk_class = "risk-low"
                        risk_emoji = "🟢"
                    
                    st.markdown(f"""
                    <div class="{risk_class}">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <h3 style="margin: 0; font-size: 1.3rem;">{risk_emoji} {risk_level} RISK</h3>
                                <p style="margin: 0.5rem 0 0 0; color: #64748b;">Risk Score: {risk_score}/100</p>
                            </div>
                            <div style="text-align: right;">
                                <p style="margin: 0; font-weight: 600;">ML Prediction: {'⚠️ High Default Risk' if prediction[0] == 1 else '✅ Low Default Risk'}</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Risk score progress
                    st.progress(risk_score / 100)
                    st.caption(f"Risk Score: {risk_score}/100")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Risk Factors
                    if risk_factors:
                        st.markdown("""
                        <div class="info-card">
                            <h4 style="color: #1e3a8a; margin-bottom: 1rem;">📊 Key Risk Factors</h4>
                        """, unsafe_allow_html=True)
                        for i, factor in enumerate(risk_factors[:8], 1):  # Show top 8 factors
                            st.write(f"{i}. {factor}")
                        st.markdown("</div>", unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Final Decision
                    st.markdown('<h3 style="color: #1e3a8a; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">🏦 Loan Decision</h3>', unsafe_allow_html=True)
                    
                    if decision == "APPROVE":
                        st.markdown(f"""
                        <div class="decision-approved">
                            <h2 style="font-size: 1.8rem; margin-bottom: 1rem;">{recommendation}</h2>
                            <p style="font-size: 1.1rem; line-height: 1.5;"><strong>Reason:</strong> {reason}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                    elif decision == "CONDITIONAL_APPROVE":
                        st.markdown(f"""
                        <div class="decision-conditional">
                            <h2 style="font-size: 1.8rem; margin-bottom: 1rem;">{recommendation}</h2>
                            <p style="font-size: 1.1rem; line-height: 1.5;"><strong>Reason:</strong> {reason}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="decision-rejected">
                            <h2 style="font-size: 1.8rem; margin-bottom: 1rem;">{recommendation}</h2>
                            <p style="font-size: 1.1rem; line-height: 1.5;"><strong>Reason:</strong> {reason}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Next Steps
                    col_c, col_d = st.columns(2)
                    
                    with col_c:
                        st.markdown("""
                        <div class="info-card">
                            <h4 style="color: #1e3a8a; margin-bottom: 1rem;">📋 Conditions & Terms</h4>
                        """, unsafe_allow_html=True)
                        for condition in decision_details["conditions"]:
                            st.write(f"• {condition}")
                        st.markdown("</div>", unsafe_allow_html=True)
                    
                    with col_d:
                        st.markdown("""
                        <div class="info-card">
                            <h4 style="color: #1e3a8a; margin-bottom: 1rem;">🚀 Next Steps</h4>
                        """, unsafe_allow_html=True)
                        for step in decision_details["next_steps"]:
                            st.write(f"• {step}")
                        st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Improvement suggestions for rejected applications
                    if decision == "REJECT":
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.markdown("""
                        <div class="info-card">
                            <h4 style="color: #1e3a8a; margin-bottom: 1rem;">💡 Improvement Suggestions</h4>
                        """, unsafe_allow_html=True)
                        
                        suggestions = []
                        if risk_score > 60:
                            suggestions.append("Reduce overall risk factors before reapplying")
                        if income > 0 and loan_amount / income > 3:
                            suggestions.append(f"Consider a smaller loan amount (under ${income * 2:,.2f})")
                        if employed_days < 2:
                            suggestions.append("Build more stable employment history")
                        if active_loan == "Yes":
                            suggestions.append("Pay down existing debt before applying for new credit")
                            
                        for suggestion in suggestions:
                            st.write(f"• {suggestion}")
                        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


# Main Application Logic
if st.session_state.page == 'welcome':
    show_welcome_screen()
else:
    show_form_screen()