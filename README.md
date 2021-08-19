# Bluebox

I created this project due to the difficulty involved in booking US visa interview slots. During COVID, the consulate was closed and interview slots were released in very limited numbers. This is a python program used to check if appointments are available at CGI Federal website. It takes an initial screenshot of the appointments page and then refreshes the page at intervals. After each refresh, it takes a new screenshot and compares it with the initial screenshot. If there is a difference, then the computer will start beeping.

As this program is using screenshots to find updates on the webpage, it is very easy to modify this program and use it on any other website.

## What is Bluebox

Knowing about the concept of bluebox was very critical while we were trying to book Visa Interview Slots. Usually, you can access the visa interview slots page only after paying for the interview. So, if you create an account in the visa interview slots booking website using some alternate email, then you cannot access or view the interview slots availability. But even when logged in using these kind of accounts, you can see a blue box in the home page of your account if there is a slot available. This blue box will have the earliest available slot. I created this program based on snapshot comparison because I will never get to inspect a bluebox to get it with ID or attributes to be added in the program :D. Because if there is a bluebox, then I would have to rush and login to book that appointment. So, I solved this problem using the snapshot comparison method.
