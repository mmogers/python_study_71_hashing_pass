# Oooh, Salty!

Hashing is great, but enterprising hackers have created their own database containing hashes of pretty much every word and common password around.

So chances are, if you use a common password or everyday word, then there's a hash of it sitting around on the internet somewhere just waiting for a reverse lookup.

To help combat this, we can generate a random value and append it to the end of your password before hashing.  This random value is called a **salt**.

👉 Let's salt our password hash from before.

```python
from replit import db

password = "Baldy1"
salt = 10221

newPassword = f"{password}{salt}" # append the salt
newPassword = hash(newPassword) # hash the lot

print(newPassword)
```
## Second User
👉 If we have a second user with the same password, the uniquely generated salt (I've just made them up in these examples) will produce a *completely different hash*. 
```python
from replit import db

password = "Baldy1"
salt = 10221
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)

password = "Baldy1"
salt = 39820
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)
```

👉 To deal with this, we'd need our database to store the hashed password **and** the salt. We do this using a dictionary.

```python
from replit import db

password = "Baldy1"
salt = 10221
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)

db["david"] = {"password":newPassword, "salt": salt}

```

👉 Now let's update the login system to pull the salt from the database, append it to the password entered and then hash the lot. After that, we can compare it to the stored hash of password and salt from the previous example.

```python
from replit import db

ans = input("Password >") # Get the input
salt = db["david"]["salt"] # Get the salt from the database.
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) # Hash the concatenated string

if newPassword == db["david"]["password"]: #compare hash of newPassword to stored hash.
  print("Login successful")

```

### Try it out!