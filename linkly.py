import pyshorteners
import validators
from termcolor import colored

def validate_url(url):
    # First, check the format using validators
    if not validators.url(url):
        return False
    return True


def shorten_url():
    # Create an instance of the Shortener class
    shortener = pyshorteners.Shortener()

    # Input the URL to shorten
    long_url = input(colored("  Enter the URL to shorten: ", "light_grey")).strip()
    if len(long_url) == 0:
        print(colored(f"\n  - Kindly enter a URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ).\n", "yellow"))
    elif validate_url(long_url):
        print(colored(f"  - Shortened URL (TinyURL): {colored(shortener.tinyurl.short(long_url), "light_green")}.\n","green"))
    else:
        print(colored(f"\n  - Invalid URL Entered: '{long_url}'.\n", "red"))

def main():
    shorten_url()

if __name__ == '__main__':
    print(colored(fr"""
                  
  ██╗     ██╗███╗   ██╗██╗  ██╗██╗  ██╗   ██╗
  ██║     ██║████╗  ██║██║ ██╔╝██║  ╚██╗ ██╔╝
  ██║     ██║██╔██╗ ██║█████╔╝ ██║   ╚████╔╝ 
  ██║     ██║██║╚██╗██║██╔═██╗ ██║    ╚██╔╝  
  ███████╗██║██║ ╚████║██║  ██╗███████╗██║   
  ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   
{colored("")}
  Shorten Links with TinyURL in CLI!"
  {colored("https://github.com/saayxee/linky", "light_blue")}
                  """, "blue"))
    while True:
      main()
      print("  -------------------------------------------------\n")

