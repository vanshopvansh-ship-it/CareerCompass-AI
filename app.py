import streamlit as st
import sys
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

st.set_page_config(
    page_title="CareerCompass AI",
    page_icon="🧭",
    layout="wide"
)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API key not found. Please check your .env file.")
    st.stop()

client = Groq(api_key=api_key)
st.set_page_config(
    page_title="CareerCompass AI",
    page_icon="🧭",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080d1b, #111a35);
    color: #ffffff;
}


h1, h2, h3 {
    color: #a78bfa !important;
}

.stButton > button {
    background: linear-gradient(90deg, #6366f1, #9333ea);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 22px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #9333ea, #6366f1);
    color: white;
}

[data-testid="stMetric"] {
    background: #1c2542;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #4541a5;
}

[data-testid="stSidebar"] {
    background: #10182e;
}

.stTextInput input {
    background: #1c2542;
    color: white;
}

.stSelectbox div[data-baseweb="select"] {
    background: #1c2542;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
    text-align:center;
    padding:45px 15px;
    background:linear-gradient(120deg,#172554,#312e81,#581c87);
    border-radius:20px;
    margin-bottom:25px;
">
    <h1 style="color:white !important;font-size:42px;">
        🚀 CareerCompass AI
    </h1>
    <h3 style="color:#c4b5fd !important;">
        Discover Your Future. Build Your Career.
    </h3>
    <p style="color:white;font-size:17px;">
        Your Smart Career Guidance Platform
    </p>
</div>
""", unsafe_allow_html=True)

st.title("🧭 CareerCompass AI")
st.subheader("Discover Your Strengths. Explore Your Future.")
st.write("Find career options based on your interests and favourite subjects.")

st.divider()

name = st.text_input("Enter your name")

education = st.selectbox(
    "Select your education level",
    ["Class 9-10", "Class 11-12", "College Student"]
)

interests = st.multiselect(
    "What are your interests?",
    ["Technology", "Problem Solving", "Creativity",
     "Research", "Healthcare", "Helping People",
     "Business", "Art"]
)

subjects = st.multiselect(
    "Select your favourite subjects",
    ["Mathematics", "Physics", "Chemistry", "Biology",
     "Computer Science", "Economics", "Commerce", "Arts"]
)

careers = {
    "Software Developer": ["Technology", "Problem Solving", "Computer Science", "Mathematics"],
    "Data Analyst": ["Technology", "Research", "Mathematics", "Economics"],
    "Graphic Designer": ["Creativity", "Art"],
    "Doctor": ["Healthcare", "Helping People", "Biology", "Chemistry"],
    "Mechanical Engineer": ["Problem Solving", "Technology", "Physics", "Mathematics"],
    "Business Analyst": ["Business", "Research", "Economics", "Commerce"],
    "Teacher": ["Helping People", "Arts"],
    "Entrepreneur": ["Business", "Creativity", "Commerce"]
}

if st.button("Explore My Careers"):
    if not name or not interests or not subjects:
        st.warning("Please enter your name and select your interests and subjects.")
    else:
        st.success(f"Hello {name}! Here are your career suggestions:")

        scores = {}

        for career, requirements in careers.items():
            score = len(set(interests + subjects) & set(requirements))
            scores[career] = score

        results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        for career, score in results[:3]:
            st.subheader("🎯 " + career)
            st.write(f"Your matching points: {score}")
            st.progress(score / 4)
            st.write("Explore the skills, courses and qualifications needed for this career.")
# Skills Analysis and Learning Roadmap

        best_career = results[0][0]

        career_details = {
            "Software Developer": {
                "skills": ["Python", "C++", "Problem Solving", "DSA"],
                "roadmap": ["Learn Python basics",
                            "Learn Data Structures",
                            "Build small projects",
                            "Learn Web Development"]
            },
            "Data Analyst": {
                "skills": ["Python", "Excel", "SQL", "Statistics"],
                "roadmap": ["Learn Excel",
                            "Learn Python",
                            "Learn SQL",
                            "Create data analysis projects"]
            },
            "Graphic Designer": {
                "skills": ["Creativity", "Canva", "Figma", "Design"],
                "roadmap": ["Learn design basics",
                            "Practice Canva",
                            "Learn Figma",
                            "Build a portfolio"]
            },
            "Doctor": {
                "skills": ["Biology", "Chemistry", "Communication"],
                "roadmap": ["Study Biology and Chemistry",
                            "Prepare for NEET",
                            "Complete medical education",
                            "Complete clinical training"]
            },
            "Mechanical Engineer": {
                "skills": ["Physics", "Mathematics", "CAD", "Design"],
                "roadmap": ["Learn Engineering Mathematics",
                            "Study Mechanics",
                            "Learn CAD software",
                            "Build engineering projects"]
            },
            "Business Analyst": {
                "skills": ["Business", "Excel", "SQL", "Communication"],
                "roadmap": ["Learn business basics",
                            "Master Excel",
                            "Learn data analysis",
                            "Practice case studies"]
            },
            "Teacher": {
                "skills": ["Communication", "Subject Knowledge",
                           "Teaching", "Creativity"],
                "roadmap": ["Master your subject",
                            "Improve communication",
                            "Learn teaching methods",
                            "Gain teaching experience"]
            },
            "Entrepreneur": {
                "skills": ["Business", "Creativity", "Leadership"],
                "roadmap": ["Find a business idea",
                            "Research the market",
                            "Create a business plan",
                            "Build a small project"]
            }
        }

        st.divider()
        st.header("📊 Your Skills Analysis")

        details = career_details[best_career]

        st.subheader("Recommended Skills")
        for skill in details["skills"]:
            st.write("✅", skill)

        st.subheader("🎯 Your Learning Roadmap")
        for i, step in enumerate(details["roadmap"], 1):
            st.write(f"Step {i}: {step}")

        st.success("Your learning journey starts today!")
        st.divider()

st.header("📈 Career Progress Tracker")

st.write("Track your learning progress!")

progress = st.slider(
    "How much of your learning roadmap have you completed?",
    0, 100, 0
)

st.progress(progress)

st.write(f"Your progress: {progress}%")

if progress < 30:
    st.info("Keep learning! You are just getting started.")
elif progress < 70:
    st.info("Good progress! Keep moving forward.")
else:
    st.success("Excellent! You are close to your goal!")
st.divider()
st.divider()

st.header("🤖 AI Career Assistant")
st.write("Ask anything about your career. Powered by Groq AI.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

user_question = st.chat_input("Ask your career question...")

if user_question:
    st.session_state.chat_history.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.write(user_question)

    try:
        with st.chat_message("assistant"):
            with st.spinner("AI is thinking..."):

                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are CareerCompass AI, a helpful career "
                            "guidance assistant for students. Give clear, "
                            "friendly and personalized career advice. "
                            "Explain skills, courses, projects and roadmaps "
                            "in simple language."
                        )
                    }
                ]

                messages.extend(st.session_state.chat_history)

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1000
                )

                answer = response.choices[0].message.content
                st.write(answer)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as e:
        st.error(f"AI Error: {e}")

    st.rerun()

if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
st.divider()

st.header("📚 Recommended Courses")

course_data = {
    "Software Developer": [
        "Python Programming",
        "C++ Programming",
        "Data Structures and Algorithms",
        "Web Development"
    ],
    "Data Analyst": [
        "Advanced Excel",
        "Python for Data Analysis",
        "SQL",
        "Power BI"
    ],
    "Graphic Designer": [
        "Canva",
        "Adobe Photoshop",
        "Figma",
        "UI/UX Design"
    ],
    "Mechanical Engineer": [
        "AutoCAD",
        "SolidWorks",
        "Engineering Mechanics"
    ],
    "Business Analyst": [
        "Excel",
        "SQL",
        "Power BI",
        "Business Analytics"
    ]
}

selected_course_career = st.selectbox(
    "Select your career",
    list(course_data.keys())
)

st.subheader("Your Suggested Courses")

for course in course_data[selected_course_career]:
    st.write("🎓", course)
    st.divider()

st.header("💼 Internship & Job Guidance")

st.write("Explore opportunities to start your career.")

st.subheader("🌐 Useful Career Platforms")

st.markdown("[1. Internshala](https://internshala.com/)")

st.markdown("[2. LinkedIn](https://www.linkedin.com/jobs/)")

st.markdown("[3. Naukri](https://www.naukri.com/)")

st.markdown("[4. Indeed](https://in.indeed.com/)")

st.subheader("📝 Resume Preparation Tips")

resume_tips = [
    "Write a clear career objective",
    "Mention your education",
    "Add your technical skills",
    "Include college projects",
    "Mention certifications"
]

for tip in resume_tips:
    st.write("✅", tip)

st.subheader("🎯 Interview Preparation")

interview_tips = [
    "Practice self introduction",
    "Prepare technical questions",
    "Improve communication skills",
    "Research the company",
    "Practice mock interviews"
]

for tip in interview_tips:
    st.write("⭐", tip)

st.success("Start preparing for your career today!")
st.divider()

st.header("📊 CareerCompass Dashboard")

st.subheader("Your Career Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Career Options", "8")

with col2:
    st.metric("Learning Roadmap", "4 Steps")

with col3:
    st.metric("Career Progress", f"{progress}%")

st.subheader("🚀 Your Next Goals")

goals = [
    "Complete your recommended courses",
    "Practice technical skills",
    "Build your first project",
    "Prepare your resume",
    "Apply for internships"
]

for goal in goals:
    st.write("🎯", goal)

st.success("Keep learning. Your future starts here!")
# CareerCompass AI Sidebar

st.sidebar.title("🚀 CareerCompass AI")

st.sidebar.markdown("---")

st.sidebar.subheader("Your Career Guide")

st.sidebar.write("👤 Student Profile")
st.sidebar.write("🎯 Career Recommendations")
st.sidebar.write("📊 Skills Analysis")
st.sidebar.write("📚 Learning Roadmap")
st.sidebar.write("💼 Internship Guidance")
st.sidebar.write("🤖 AI Assistant")

st.sidebar.markdown("---")

st.sidebar.info(
    "Your future starts with the right career decision!"
)

st.sidebar.caption("CareerCompass AI | Version 1.0")
st.divider()

st.header("🧠 Career Assessment Quiz")

st.write("Answer these questions to explore your career interests.")

q1 = st.radio(
    "1. What do you enjoy most?",
    ["Coding", "Solving problems", "Designing", "Helping people"]
)

q2 = st.radio(
    "2. Which subject do you like?",
    ["Computer Science", "Mathematics", "Arts", "Biology"]
)

q3 = st.radio(
    "3. What is your strength?",
    ["Logical Thinking", "Creativity", "Communication", "Leadership"]
)

if st.button("Analyze My Interests 🎯"):

    score = {
        "Technology": 0,
        "Engineering": 0,
        "Design": 0,
        "Healthcare": 0
    }

    if q1 == "Coding":
        score["Technology"] += 2
    elif q1 == "Solving problems":
        score["Engineering"] += 2
    elif q1 == "Designing":
        score["Design"] += 2
    else:
        score["Healthcare"] += 2

    if q2 == "Computer Science":
        score["Technology"] += 2
    elif q2 == "Mathematics":
        score["Engineering"] += 2
    elif q2 == "Arts":
        score["Design"] += 2
    else:
        score["Healthcare"] += 2

    if q3 == "Logical Thinking":
        score["Technology"] += 1
        score["Engineering"] += 1
    elif q3 == "Creativity":
        score["Design"] += 2
    elif q3 == "Communication":
        score["Healthcare"] += 1
    else:
        score["Engineering"] += 1

    best_match = max(score, key=score.get)

    st.success(f"Your strongest interest area: {best_match}")

    st.subheader("Your Interest Analysis")
    st.bar_chart(score)

    st.info("Explore this career area further before making a final decision.")
    st.divider()
st.header("📄 AI Resume Builder")
st.write("Create your professional resume with CareerCompass AI.")

with st.form("resume_form"):
    st.subheader("Personal Details")

    resume_name = st.text_input("Full Name")
    resume_email = st.text_input("Email")
    resume_phone = st.text_input("Phone Number")
    resume_location = st.text_input("City")

    st.subheader("Education")

    resume_education = st.text_input(
        "College / School and Qualification"
    )

    resume_year = st.text_input("Passing Year")

    st.subheader("Skills and Projects")

    resume_skills = st.text_area(
        "Your Skills (comma separated)"
    )

    resume_projects = st.text_area(
        "Your Projects and Achievements"
    )

    resume_career = st.selectbox(
        "Career Goal",
        ["Software Developer", "Data Analyst",
         "AI Engineer", "Web Developer",
         "Mechanical Engineer", "Business Analyst"]
    )

    generate_resume = st.form_submit_button(
        "✨ Generate AI Resume"
    )

if generate_resume:
    if not resume_name or not resume_email or not resume_education:
        st.warning("Please fill Name, Email and Education.")
    else:
        try:
            with st.spinner("AI is creating your resume..."):

                prompt = f"""
                Create a professional student resume.

                Name: {resume_name}
                Education: {resume_education}
                Passing Year: {resume_year}
                Skills: {resume_skills}
                Projects: {resume_projects}
                Career Goal: {resume_career}

                Write a professional summary, skills,
                education and projects sections.
                Do not invent experience or qualifications.
                Use only the supplied information.
                """

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1200
                )

                resume_text = response.choices[0].message.content

            st.session_state.generated_resume = resume_text

        except Exception as e:
            st.error(f"Resume generation error: {e}")

if "generated_resume" in st.session_state:
    st.subheader("🎯 Your AI Generated Resume")
    st.write(st.session_state.generated_resume)

    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=A4)

    width, height = A4
    y = height - 50

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(45, y, "CAREERCOMPASS AI RESUME")
    y -= 35

    pdf.setFont("Helvetica", 10)

    for line in st.session_state.generated_resume.splitlines():
        line = line.encode("latin-1", "replace").decode("latin-1")

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = height - 50

        pdf.drawString(45, y, line[:100])
        y -= 16

    pdf.save()
    pdf_buffer.seek(0)

    st.download_button(
        "📥 Download Resume PDF",
        data=pdf_buffer,
        file_name="CareerCompass_Resume.pdf",
        mime="application/pdf"
    )
    # ADVANCED CAREER DASHBOARD

st.divider()
st.header("🚀 Advanced Career Analytics")

st.write("Your personalized career performance overview.")

# Career Readiness Score

profile_points = 20 if name else 0
interest_points = 20 if interests else 0
subject_points = 20 if subjects else 0
progress_points = progress * 0.20
resume_points = 20 if "generated_resume" in st.session_state else 0

readiness = int(
    profile_points + interest_points +
    subject_points + progress_points + resume_points
)

st.subheader("🎯 Career Readiness Score")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Readiness Score", f"{readiness}%")

with col2:
    st.metric("Learning Progress", f"{progress}%")

with col3:
    resume_status = (
        "Completed"
        if "generated_resume" in st.session_state
        else "Pending"
    )
    st.metric("Resume Status", resume_status)

st.progress(readiness / 100)

# Career Match Analytics

st.divider()
st.subheader("📊 Career Match Analytics")

career_scores = {}

for career, requirements in careers.items():
    career_scores[career] = len(
        set(interests + subjects) & set(requirements)
    )

top_matches = sorted(
    career_scores.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

if any(score > 0 for career, score in top_matches):
    st.bar_chart({
        "Career": [career for career, score in top_matches],
        "Match Score": [score for career, score in top_matches]
    }, x="Career", y="Match Score")
else:
    st.info("Select your interests and subjects to see career analytics.")

# Skills Analytics

st.divider()
st.subheader("🧠 Skills & Interests Analytics")

st.write("Your selected interests:", ", ".join(interests) or "Not selected")
st.write("Your favourite subjects:", ", ".join(subjects) or "Not selected")

# Learning Progress Chart

st.divider()
st.subheader("📈 Learning Progress Analytics")

st.bar_chart({
    "Stage": ["Completed", "Remaining"],
    "Percentage": [progress, 100 - progress]
}, x="Stage", y="Percentage")

# Next Goals

st.divider()
st.subheader("🎯 Your Personalized Next Goals")

if readiness < 40:
    st.info("Complete your student profile and career assessment.")
elif readiness < 70:
    st.info("Improve your skills and complete your learning roadmap.")
else:
    st.success("Great progress! Continue building projects and preparing for internships.")

dashboard_goals = [
    "Complete recommended courses",
    "Practice technical skills",
    "Build portfolio projects",
    "Update your professional resume",
    "Prepare for interviews"
]

for goal in dashboard_goals:
    st.checkbox(goal, key="dashboard_" + goal)

st.success("CareerCompass AI Analytics Dashboard is ready!")