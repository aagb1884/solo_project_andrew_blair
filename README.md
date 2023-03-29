Barry Chips' Barry Chip Emporium *

Andrew Blair’s CodeClan Solo Project

This application simulates a chip shop website, with the functionality to show a menu, all orders, and individual orders. You can update and delete orders too. The function to create an order function is unfinished.

This was done using Python, SQL, CSS, HTML, Flask and psycogb2 as part of a solo project on the Software Development course at CodeClan, Edinburgh. The aim of the project was to cement my understanding of Restful Routes and CRUD actions, with further practice what we have learned from the Python module (most recently using SQL, in this case with many to many relationships involved). 

The Create function has proved especially tricky due to the SQL table for Orders not including the food requested. Instead this needs to come in from the third table (Orders and Items being the first two, one Order can have many Items). The basic structure of the site was, however, fairly straightforward to achieve.

The CSS is also quite successful, being mostly accessible. With further time I hope to improve accessibility, complete the Create Order function and include total costs of Orders (possibly with discounts when you spend over a certain amount). I also hope to update the order form so you can order multiples of items.

HOW TO RUN THE APP

You will need to have Flask and psycogb2 installed. 

1. Download the repo.
2. Use the terminal to move to the repo folder and then enter 'Flask Run'.
3. This will allow you to view the app in your browser using the HOST and PORT numbers in the .flaskenv file.

HOW TO USE THE APP

The Emporium currently has a basic chip shop set up. This can be expanded, but on the understanding that this is a chip emporium and therefore all Items must heavily involve chips.

On the Home page is a nav bar (with links to the home page, the Menu, and the existing orders). There is also link saying ORDER NOW. This will take you to an order form. You can also access this from the Menu page.

You can enter your contact details (make some up please, don't use your actual address) and select which items you want to order. Once you have placed your order you can find it on the Orders page, select it, and then edit or delete it.

Attribution-ShareAlike
CC BY-SA

* for those of you who don’t understand Edinburgh slang, this is quite funny.
