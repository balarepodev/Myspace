from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Database connection function
def get_db_connection():
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=PHOENIX;"
        "DATABASE=testdb;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(connection_string)

# Route to retrieve data from SQL Server
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Example query
    cursor.execute("SELECT * FROM dbo.employee")
    
    rows = cursor.fetchall()
    conn.close()
    
    # Pass the retrieved rows to the HTML template
    return render_template('index.html', rows=rows)
    
   # Route to handle form submission and update the database
@app.route('/update', methods=['POST'])
def update():
    id = request.form['EID']
    new_role = request.form['ERole']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL command to update the database
    cursor.execute("UPDATE dbo.employee SET ERole = ? WHERE EID = ?", (new_role, id))
    conn.commit()  # Commit the changes
    conn.close()
    
    return redirect(url_for('index'))  # Redirect back to the main page


if __name__ == "__main__":
    app.run(debug=True)