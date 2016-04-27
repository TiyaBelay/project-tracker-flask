from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""
    #why do we need a placeholder for the gthub name?
    github = request.args.get('github')
    first, last, github = hackbright.get_student_by_github(github)
    project_grade = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github,
                            project_grade=project_grade,    
                            )
    return html
    # return "%s is the GitHub account for %s %s" % (github, first, last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add")
def get_new_student():
    """Show form for searching for a student."""

    return render_template("student_add.html")


@app.route("/student-added", methods=['POST'])
def added_new_student():
    """Show form to add a new student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')
   
    hackbright.make_new_student(first, last, github)

    return render_template("student_added.html", 
                            first=first,
                            last=last,
                            github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
