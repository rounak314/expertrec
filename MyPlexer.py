class MyPlexer:

    def route(self,param):

        def decorator_function(original_function):

            def inner_function(*args , **kwargs):

                result = original_function()
                print(result)
                return result

            return inner_function
            
        return decorator_function