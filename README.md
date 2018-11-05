# Logs Analysis Project

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.
The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.
###### it is a required project for Udacity's Front-End Nanodegree Program.
###### it was developed by Osama Aloqaily,
https://github.com/o-aloqaily

## Steps To Run the Project
##### Download and setup
  - Install [VirtualBox](https://www.virtualBox.org) & [Vagrant](https://www.vagrantup.com)
  - Download [needed virtual machine configuration files](https://github.com/udacity/fullstack-nanodegree-vm)
  - Download [needed database data setup (sql files)](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  - Move all sql files you downloaded in the last step into the vagrant directory, which is inside the virtual machine configuration files you downloaded in the second step.
  - Download this project if you didn't.

##### Loading and running the program
  - using the terminal, navigate (cd) to the vagrant directory inside the virtual machine folder.
  - Run `vagrant up` then `vagrant ssh`.
  - navigate (cd) into this project directory inside the virtual machine (second last step on Download and setup)
  - run the following command to load the pre-required data for this project:
  `psql -d news -f newsdata.sql`
  - Finally! Run the project using: `python project.py`
