def outer(message):
    print('In the outer function')

    def inner():
        print('Calling the inner funcation')
        print(message)
    return inner()

f = outer("Hello World")
(f)

def decorator(original_func):
    print('In the deorator funcation\n')
