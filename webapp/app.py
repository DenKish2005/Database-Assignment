from flask import Flask, render_template, request, redirect, url_for, abort
from datetime import datetime
from models import db, User, Caregiver, Member, Address, Job, JobApplication, Appointment
          
app = Flask(__name__)       
                  
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:Gumballdarwin1385@localhost:5432/care_platform_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False            
            
db.init_app(app)           
            
MODELS = {
    "user": (User, "user_id"),      
    "caregiver": (Caregiver, "caregiver_user_id"),    
    "member": (Member, "member_user_id"),     

    "address": (Address, "member_user_id"),      
    "job": (Job, "job_id"),       
    "appointment": (Appointment, "appointment_id"),  
    "job_application": (JobApplication, None),    
} 


FIELDS = {      
    "user": ["email","given_name","surname","city","phone_number","profile_description","password"],
    "caregiver": ["caregiver_user_id","photo","gender","caregiving_type","hourly_rate"],
    "member": ["member_user_id","house_rules","dependent_description"],

    "address": ["member_user_id","house_number","street","town"],   
    "job": ["member_user_id","required_caregiving_type","other_requirements","date_posted"],
    "appointment": ["caregiver_user_id","member_user_id","appointment_date","appointment_time","work_hours","status"],
    "job_application": ["caregiver_user_id","job_id","date_applied"],
}

@app.before_request 
def create_tables_once():       

    with app.app_context():
        db.create_all()     

@app.route("/") 
def home(): 
    return render_template("home.html", models=MODELS.keys())       

@app.route("/<model_name>/")
def list_items(model_name):
    if model_name not in MODELS:
        abort(404)
    Model, pk = MODELS[model_name]
    items = Model.query.all()
    return render_template("list.html", model_name=model_name, fields=FIELDS[model_name], items=items, pk=pk)

@app.route("/<model_name>/create", methods=["GET","POST"])      
def create_item(model_name):
    if model_name not in MODELS:    
        abort(404)
    Model, pk = MODELS[model_name]
    fields = FIELDS[model_name] 

    if request.method == "POST":        
        data = {}
        for f in fields:
            data[f] = request.form.get(f) or None


        if "date_posted" in data and data["date_posted"]:
            data["date_posted"] = datetime.strptime(data["date_posted"], "%Y-%m-%d").date()
        if "appointment_date" in data and data["appointment_date"]: 
            data["appointment_date"] = datetime.strptime(data["appointment_date"], "%Y-%m-%d").date()
        if "appointment_time" in data and data["appointment_time"]: 
            data["appointment_time"] = datetime.strptime(data["appointment_time"], "%H:%M").time()
        if "date_applied" in data and data["date_applied"]: 
            data["date_applied"] = datetime.strptime(data["date_applied"], "%Y-%m-%d").date()

        item = Model(**data)            
        db.session.add(item)        
        db.session.commit()
        return redirect(url_for("list_items", model_name=model_name))

    return render_template("form.html", action="create", model_name=model_name, fields=fields, item=None)

@app.route("/<model_name>/<pk_value>/edit", methods=["GET","POST"])
def edit_item(model_name, pk_value):
    if model_name not in MODELS:    
        abort(404)

    Model, pk = MODELS[model_name]
    fields = FIELDS[model_name]

    if pk is None:      
        abort(400)  

    item = Model.query.get_or_404(pk_value)

    if request.method == "POST":
        for f in fields:
            if f == pk: 
                continue        
            val = request.form.get(f) or None
            if f in ["date_posted","appointment_date","date_applied"] and val:
                val = datetime.strptime(val, "%Y-%m-%d").date()
            if f == "appointment_time" and val:
                val = datetime.strptime(val, "%H:%M").time()
            setattr(item, f, val)

        db.session.commit()
        return redirect(url_for("list_items", model_name=model_name))

    return render_template("form.html", action="edit", model_name=model_name, fields=fields, item=item)

@app.route("/<model_name>/<pk_value>/delete", methods=["POST"])
def delete_item(model_name, pk_value):
    if model_name not in MODELS:
        abort(404)

    Model, pk = MODELS[model_name]
    if pk is None:
        abort(400)

    item = Model.query.get_or_404(pk_value)
    db.session.delete(item)     
    db.session.commit()
    return redirect(url_for("list_items", model_name=model_name))




@app.route("/job_application/<caregiver_id>/<job_id>/edit", methods=["GET","POST"])
def edit_job_application(caregiver_id, job_id):
    item = JobApplication.query.get_or_404((caregiver_id, job_id))
    fields = FIELDS["job_application"]

    if request.method == "POST":
        val = request.form.get("date_applied") or None
        if val:
            item.date_applied = datetime.strptime(val, "%Y-%m-%d").date()
        db.session.commit()
        return redirect(url_for("list_items", model_name="job_application"))

    return render_template("form.html", action="edit", model_name="job_application", fields=fields, item=item)

@app.route("/job_application/<caregiver_id>/<job_id>/delete", methods=["POST"])
def delete_job_application(caregiver_id, job_id):
    item = JobApplication.query.get_or_404((caregiver_id, job_id))
    db.session.delete(item)     
    db.session.commit()
    return redirect(url_for("list_items", model_name="job_application"))


if __name__ == "__main__":
    app.run(debug=False)
