import os 

password = input("Masukan Password: ")
if password == "admin":
  from run import app
  if __name__ == "__main__":
       app.run(debug=True)
else:
    exit()