from fastapi import FastAPI, Request, Form
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from MLrecommendation import recommend_by_text
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="mysecretkey")
#login_data
import mysql.connector

try:
    # 🔥 CONNECT
    conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

    # 🔥 CREATE CURSOR
    cursor = conn.cursor()

    # 🔥 INSERT
    cursor.execute(
    "INSERT INTO user_history (domain, skills, location, mode, email) VALUES (%s, %s, %s, %s, %s)",
    (domain, skills, location, mode, email)
)

    conn.commit()

    # 🔥 CLOSE
    cursor.close()
    conn.close()

except Exception as e:
    print("DB ERROR:", e)


# folders
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# to run fastapi uvicorn main:app --reload is command
# ---------------- HOME PAGE ----------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("new_home_page.html", {"request": request})


# ---------------- LOGIN ----------------
@app.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    try:
        import mysql.connector

        conn1 = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
)
        cursor = conn1.cursor()

        # 🔍 Check if user exists
        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cursor.fetchone()

        if user:
            # ✅ SAVE SESSION (MISSING LINE)
            request.session["user"] = email

            cursor.close()
            conn1.close()

            return RedirectResponse(url="/details", status_code=303)

        else:
            # ➕ Register new user
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (%s, %s)",
                (email, password)
            )
            conn1.commit()

            # ✅ SAVE SESSION HERE ALSO
            request.session["user"] = email

            cursor.close()
            conn1.close()

            return RedirectResponse(url="/details", status_code=303)

    except Exception as e:
        print("LOGIN ERROR:", e)
        return templates.TemplateResponse(
            "new_home_page.html",
            {"request": request, "error": "Login failed"}
        )
# ---------------- DETAILS PAGE ----------------
@app.get("/details", response_class=HTMLResponse)
def details(request: Request):
    return templates.TemplateResponse("new_details_page.html", {"request": request})


# ---------------- RECOMMENDATION ----------------
@app.post("/recommend")
def recommend(
    request: Request,
    domain: str = Form(...),
    skills: str = Form(""),
    education: str = Form(""),
    location: str = Form(""),
    mode: str = Form(""),
    duration: str = Form(""),
    ministry: str = Form("")
):

    try:
        # 🔐 Get logged-in user
        email = request.session.get("user")

        if not email:
            return RedirectResponse(url="/", status_code=303)

        # 🔥 Clean inputs
        domain = " ".join(domain.split(","))
        skills = " ".join(skills.split(","))

        # 🔥 CONNECT TO DB
        import mysql.connector
        conn2 = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
        )

        cursor = conn2.cursor()

        # 🔥 INSERT DATA (NOW email works)
        cursor.execute(
            "INSERT INTO user_history (domain, skills, location, mode, email) VALUES (%s, %s, %s, %s, %s)",
            (domain, skills, location, mode, email)
        )

        conn2.commit()

        # 🔥 CLOSE DB
        cursor.close()
        conn2.close()

        # 🔥 ML QUERY
        query = f"{domain} {domain} {skills} {skills} {education}"

        results = recommend_by_text(query)

        # 🔥 APPLY FILTERS
        if location and location != "Any":
            results = results[results["location"] == location]

        if mode and mode != "Any":
            results = results[results["mode"] == mode]

        # 🔥 NORMALIZE SCORE
        if not results.empty:
            max_score = results["match_score"].max()
            if max_score != 0:
                results["match_score"] = (results["match_score"] / max_score * 100).round(2)

        results = results.to_dict(orient="records")

        return templates.TemplateResponse(
            "new_result_page.html",
            {"request": request, "results": results}
        )

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}