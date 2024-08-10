from flask import Flask, render_template_string
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
    
    # Display results in the browser
    table_html = "<table border='1'><tr><th>EName</th></tr>"
    for row in rows:
        table_html += f"<tr><td>{row.EName}</td></tr>"
    table_html += "</table>"
    
    return render_template_string(table_html)

if __name__ == "__main__":
    app.run(debug=True)
