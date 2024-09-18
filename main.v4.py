Skip to content
Navigation Menu
biding-on-skis
/
main_assesment_resub

Type / to search
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Creating a new file in main_assesment_resub
Breadcrumbsmain_assesment_resub
/
Name your file...
in
main

Edit

Preview
Indent mode

Spaces
Indent size

2
Line wrap mode

No wrap
Editing file contents
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
import time
import pandas as pd


# checks if numbers entered
def num_checker(question, low, high):
    while True:
        error = f"Enter a valid option between {low} and {high}"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)


# allows for single letter input
def string_checker(question, valid_ans):
    error = f"Enter a valid option from {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)


# doesn't allow for blank response
def not_blank(question):
    error = "Please give a valid answer."
    while True:
        user_name = input(question)
        if user_name != '':
            return user_name
        else:
            print(error)


# checks for size of curry (small medium large)
def curry_size_checker(curry_size):
    if curry_size == "small":
        return 10
    elif curry_size == "medium":
        return 15
    else:
        return 20


# checks for size of drink (can bottle)
def drink_size_checker(drink_size):
    if drink_size == "can":
        return 3.3
    else:
        return 5


# checks number and displays corresponding flavour
def curry_selector(curry):
    curry_names = {
        1: "Chicken Tikka Masala",
        2: "Korma",
        3: "Rogan Josh",
        4: "Butter Chicken",
        5: "Madras",
        6: "Chicken Curry",
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
New File at / · biding-on-skis/main_assesment_resub
