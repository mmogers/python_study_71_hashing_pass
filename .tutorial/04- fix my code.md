# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) 

if ans == db[david]["password"]: 
  print("Login successful")
```

<details> <summary> 👀 Answer </summary>

```python
from replit import db

ans = input("Password >") 
salt = db["david"]["salt"] 
newPassword = f"{ans}{salt}" # salt goes on the end of the password
newPassword = hash(newPassword) 

if newPassword == db["david"]["password"]: # uce newPassword in the comparison.  Put the key in quotes.
  print("Login successful")
```

</details>