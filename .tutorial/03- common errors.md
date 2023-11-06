# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## It's Not Logging Me In

👉 What's the problem here?


```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"]
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) 

if ans == db["david"]["password"]: 
  print("Login successful")
```

<details> <summary> 👀 Answer </summary>

We were checking the *pre hashed* input in the 'ans' variable instead of the *post hashed* data in the 'newPassword' variable.

```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) 

if newPassword == db["david"]["password"]: #compare hash of newPassword to stored hash.
  print("Login successful")
```

</details>

## Hold The Salt

👉 What is the problem here?
```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{salt}{ans}"
newPassword = hash(newPassword) 

if newPassword == db["david"]["password"]: 
  print("Login successful")
```

<details> <summary> 👀 Answer </summary>

We've concatenated the salt at the beginning of the password in the fString. It should go on the end.

```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{ans}{salt}" # the salt should go on the end of the password
newPassword = hash(newPassword) 

if newPassword == db["david"]["password"]: 
  print("Login successful")
```


</details>

