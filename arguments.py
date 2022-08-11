def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "country" in keys:
       return f"Hello {kwargs['name']} you are from {kwargs['country']}"
    elif "name" in keys:
        return f"Hello {kwargs['name']}"
    elif "age" in keys:
        year=2022-age
        return f"Hello {kwargs['name']} you were born in{year}"
    else:
        return "Hello anonymous"
 
    
    
    
