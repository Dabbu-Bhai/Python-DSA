def func():
    global count
    if count <4:
        print("Hello")
        count+=1
        func()
    return

count = 0
func()