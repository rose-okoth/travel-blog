# Project Name

The Wanderer Blog
​
# Project Description

This an app where users who love to travel can blog about places they've been to, as well as see and read blog posts from other travellers.

# Author(s) Information

> Rose Okoth.
​
# Screenshots

![Alt text](/static/images/Screenshot.png?raw=true "Landing Page")

![Alt text](/static/images/Screenshot-1.png?raw=true "Blog Post")

# BDD

* Users should be able to:
    - view the blog posts on the site.
    - search through posts by titles, author or blog content.
    - register an account.
    - create their own blog posts .
    - login and logout to read other posts.
    - make post drafts to be posted on later dates.
    - update and delete posts.

# Setup Instructions

1. Clone the repo:
   * `git clone https://github.com/rose-okoth/travel-blog.git`
​
1. Switch into the directory:
   * `cd travel-blog`
​
# Running the Application

1. Create the virtual environment
   * ` $ python3 -m venv venv `
   * ` $ source venv/bin/env `

1. Installing dependencies
   * ` $ pip install -r requirements.txt`

1. Setting up the database
    * `$ setup your database`
    * `$ python3 manage.py makemigrations travel`
    * `$ python3 manage.py migrate`

1. To run the application, in your terminal:
    * `python3 manage.py runserver`

# Testing the Application

1. To run the tests for app:
    * `$ python3 manage.py test`
    
# Technologies Used

* Python3.
* Django.
* HTML.
* Bootstrap.
* JQuery.
* CSS.
​
# Contact Information

* Email: [Email](mailto:okoth.rose0@gmail.com)
* Phone number: [Phone](tel:+254712476547)
​
# License and Copyright Information
​
Copyright(c) 2021 - Rose Okoth.  
​
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
​
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
​
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
​
Reference: [MIT License](https://opensource.org/licenses/MIT)
