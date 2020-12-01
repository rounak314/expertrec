<h1>Problem Statement :</h1> 
Write a small multiplexer library that takes commands from the input stream (console) and then print the output provided by a handler that is registered with the library.

This problem was basically a concept of decorator function, where route() was the outermost decorator.

Decorator :
Decorators allow programmers to modify the behavior of a function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

<h1>How to Run the code :</h1>
<ul>
<li>Pull the code from the repository.</li>
    # git clone repo_name
    # git pull origin master
<li>Change the directory to the git directory in the terminal.</li>
<li>Write the below code:</li>
    # python app.py message
</ul>

As of now the code can respond to only two messages “hello” and “bye”.
more instructions can be added.

<h1>Steps to add more responses :</h1>

‘’’
  @app.route(‘message’)
   def message():
    return reply
‘’’
