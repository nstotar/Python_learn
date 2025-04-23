# Step 1: Create or reset the file using 'w' mode
with open("demoText.txt", "w") as f:
    f.write("Hello\nWorld\n")
print("Initial content written with 'w' mode.")

# 'r' mode – Read only
with open("demoText.txt", "r") as f:
    print("\n[r] Read-only mode output:")
    print(f.read())

# 'a' mode – Append only
with open("demoText.txt", "a") as f:
    f.write("Appended using 'a' mode\n")
print("\n[a] Line appended using append mode.")

# 'r+' mode – Read and Write (does not clear content)
with open("demoText.txt", "r+") as f:
    print("\n[r+] Before write:")
    print(f.read())
    f.seek(0)  # Move cursor to start
    f.write("Start")  # Overwrites from the beginning
print("[r+] Overwrote beginning of the file.")

# 'w+' mode – Write and Read (clears all content)
with open("demoText.txt", "w+") as f:
    f.write("This is written by w+ mode\n")
    f.seek(0)
    print("\n[w+] After write and read:")
    print(f.read())
print("[w+] File overwritten and read.")

# 'a+' mode – Append and Read
with open("demoText.txt", "a+") as f:
    f.write("This is appended by a+ mode\n")
    f.seek(0)
    print("\n[a+] File content after appending:")
    print(f.read())
print("[a+] File appended and read.")

# Final content preview
with open("demoText.txt", "r") as f:
    print("\n📄 Final content of demoText.txt:")
    print(f.read())


"""

[r] Read-only mode output:
Hello
World


[a] Line appended using append mode.

[r+] Before write:
Hello
World
Appended using 'a' mode

[r+] Overwrote beginning of the file.

[w+] After write and read:
This is written by w+ mode

[w+] File overwritten and read.

[a+] File content after appending:
This is written by w+ mode
This is appended by a+ mode

[a+] File appended and read.

📄 Final content of demoText.txt:
This is written by w+ mode
This is appended by a+ mode 

"""


