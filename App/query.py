import pyrebase

config = {
  "apiKey": "AIzaSyA039WLLPkdWZeSpCSc6ilUgygLgSgGylg",
  "authDomain": "highonbot-fee46.firebaseapp.com",
  "databaseURL": "https://highonbot-fee46.firebaseio.com",
  "storageBucket": "highonbot-fee46.appspot.com"
}

emailId = "teamanything98@gmail.com"
password = "@random_bits" 

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(emailId,password)

# Get a reference to the database service
db = firebase.database()

def refresh(user):
    user=auth.refresh(user['refreshToken'])

def addUser(senderId,SSH,userid,password):
  print("="*100)
  refresh(user)
  print("="*100)
  users=db.get(user['idToken']).val()
  print("="*100)
  users[senderId]=[SSH,userid,password]
  db.update(users)
  print("="*100)

def getUser(senderId):
  refresh(user)
  users=db.get(user['idToken']).val()
  return users[senderId]

if __name__ == "__main__":
  addUser("123","1912","1021","@dhw9hd")