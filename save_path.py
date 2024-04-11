def save_path(directory, filename):
    '''return a path to save a file in a directory os independent. If the directory does not exist, it will be created.'''
    #based on https://www.btelligent.com/en/blog/best-practice-working-with-paths-in-python-part-1-2/ and https://www.tutorialsfreak.com/python-tutorial/examples/create-directory
    import os
    if not os.path.exists(directory): os.makedirs(directory)
    return os.sep.join([directory, filename])