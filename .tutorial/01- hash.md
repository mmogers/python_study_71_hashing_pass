# It's Called Hashing

One of the big issues with storing usernames and passwords in a database is *what happens if we're hacked*?

If those passwords are stored as text, our users' security is compromised. Probably across multiple sites because they **ignored our advice and used the same password for everything!!!!!**


## Hashing

In reality, organizations *don't store your actual password*. They store a hash of your password. A hash is produced by turning your password into a sequence of numbers, then passing it though a hashing algorithm (some mathematical process that is very difficult to reverse engineer). The data spit out of this hashing algorithm is what's stored instead of your actual password.

👉 So let's do it. I'm using the built-in `hash` function to create a numerical hash of the password. 

```python
password = "baldy1"
password = hash(password)
print(password)

# This will output a really long number

```
Play around with different strings on line 1 and notice how the hash number completely changes.

👉 Now let's store that hashed version in our database instead of the actual password.

```python
from replit import db

userName = "david"
password = "baldy1"
password = hash(password)
db[userName] = password # Stores the hashed password in the database under the username key 'david'

print(password)
```

## Printing the Hash
👉 Now I can output the value from the database using print. Notice how it outputs the hash.  That will be useless to a hacker. They cannot easily reverse engineer the password from the hash.

```python
from replit import db

print(db["david"])

```

To login a user, we get their password, input it, hash it, and compare it to the hash stored in the database because **a string will always produce the same hashed value**.

👉 Let's build the login system that checks the stored hash against a hash of the input.

```python
from replit import db

ask = input("Password >") # Get the input
ask = hash(ask) # Hash the input

if ask == db["david"]: #compare hash of input to stored hash.
  print("Login successful")

```


### Try it out!