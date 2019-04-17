"""
This script runs the My_site application using a development server.
"""

from Room_App import app

if __name__ == "__main__":
    app.run(debug=True, port=8000)