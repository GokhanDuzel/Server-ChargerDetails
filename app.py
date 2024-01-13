from backend import app

if __name__ == '__main__': 
    print("charging station details microservice.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)