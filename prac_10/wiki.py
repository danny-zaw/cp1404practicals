"""
CP1404 - Practical 10
Wiki Program
"""

import wikipedia

def main():
    page_title = input("Enter page title: ")
    while page_title != "":
        try:
            page = wikipedia.page(page_title)
            print(f"{page.title}\n{page.summary}\n{page.url}\n")
        except wikipedia.exceptions.PageError:
            print(f"Page id \"{page_title}\" does not match any pages. Try another id!")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following, or a new search:\n{e.options}")
        page_title = input("Enter page title: ")
    print("Thank you.")

main()