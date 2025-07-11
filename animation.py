import os
import time

# ANSI escape codes for color
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def center_text(text, width=70):
    return text.center(width)

def display_custom_output():
    os.system("cls" if os.name == "nt" else "clear")

    banner = f"""{GREEN}
  8b           d8   ,ad8888ba,        88       88888888ba,    
  `8b         d8'  d8"'    `"8b       88       88      `"8b   
   `8b       d8'  d8'        `8b      88       88        `8b  
    `8b     d8'   88          88      88       88         88  
     `8b   d8'    88          88      88       88         88  
      `8b d8'     Y8,        ,8P      88       88         8P  
       `888'  888  Y8a.    .a8P  888  88  888  88      .a8P   
        `8'   888   `"Y8888Y"'   888  88  888  88888888Y"'    
{RESET}"""

    print(banner)

    # Show alt link and link
    print(f"{CYAN}alt link :: {YELLOW}http://127.0.0.1:80")
    print(f"{CYAN}link     :: {YELLOW}http://voidchat.local{RESET}\n")

    # Centered thank you
    time.sleep(0.2)
    print(center_text(f"{BOLD}{GREEN}Thank you for using our project!{RESET}"))

# Entry point for .bat
if __name__ == "__main__":
    display_custom_output()
