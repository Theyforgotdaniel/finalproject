from flask import Blueprint, render_template, request, url_for, redirect

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("login.html", email="skibidi@gmail.com")

@views.route("/security-settings", methods=["POST", "GET"])
def securitysettings():
    if request.method == "POST":
        if request.form["action"] == "save":
            email = request.form["email"]
            phone_number = request.form["phone_number"]
            password = request.form["password"]
            new_password = request.form["new_password"]
            return redirect(url_for("views.display_securitysettings", email=email, phone_number=phone_number, password=password, new_password=new_password))
        elif request.form["action"] == "cancel":
            return redirect(url_for("views.home"))
    else:
        return render_template("securitysettings.html")

@views.route("/display-securitysettings")
def display_securitysettings():
    email = request.args.get("email")
    phone_number = request.args.get("phone_number")
    password = request.args.get("password")
    new_password = request.args.get("new_password")

    return f"""
    <h1>Security Setting Details</h1>
    <p>email: {email}</p>
    <p>phone_number: {phone_number}</p>
    <p>password: {password}</p>
    <p>new_password: {new_password}</p>
    """

@views.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form["action"] == "save":
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            dob = request.form["dob"]
            gender = request.form["gender"]
            return redirect(url_for("views.display_accountdetails", first_name=first_name, last_name=last_name, dob=dob, gender=gender))
        elif request.form["action"] == "cancel":
            return redirect(url_for("views.home"))
    else:
        return render_template("login.html")

@views.route("/display-accountdetails")
def display_accountdetails():
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    dob = request.args.get("dob")
    gender = request.args.get("gender")
    
    return f"""
    <h1>User Personal Details</h1>
    <p>First Name: {first_name}</p>
    <p>Last Name: {last_name}</p>
    <p>Date of Birth: {dob}</p>
    <p>Gender: {gender}</p>
    """
