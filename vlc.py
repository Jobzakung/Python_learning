from pylenium import Pylenium

# Create an instance of Pylenium
py = Pylenium()

# Open a webpage
py.visit("https://dev.playbux.co/login")

# Interact with elements
py.get("input[name='username']").type("myusername")
py.get("input[name='password']").type("mypassword")
py.get("button[type='submit']").click()

# Assert expected behavior
# Close the browser
py.quit()
