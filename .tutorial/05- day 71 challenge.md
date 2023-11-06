# 👉 Day 71 Challenge

Today's challenge is to build a simple login system.

Your program should:

1. Display a menu with the ability to add a user or login.
2. 'Add' user should:
    1. Ask for a username and password.
    2. Create a new password and a randomly generated 4 digit salt.
    3. Append the salt to the password and hash it.
    4. Store the hash and the salt in a repl db with the username as the key.
7. 'Login' should:
    1. Get username and password input.
    2. Display a success message if details are correct.
9. This system should work with multiple users.


Example:

```
🌟Login System🌟

1: Add User, 2: Login >  1

Username: > Kenny
Password: > L0gg1ns

Details stored.

1: Add User, 2: Login >  2

Username: > Kenny
Password: > L0gg1ns

Login successful
```

<details> <summary> 💡 Hints </summary>
  
- Try implementing the two menu options as subroutines. You'll be able to port them to other programs more easily. 

</details>