print("<============ TO - DO LIST ===========>")
task={}
while True:
    print("1.Add Task\n2.Show tasks\n3.Mark task as done\n4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        n=int(input("Enter the numer of tasks:"))
        for i in range(0,n):
            t=input("Enter the task:")
            task[t]="not done"
            print("Task added!")
    elif ch==2:
        i=1
        for key,value in task.items():
            print(i,".",key,"-",value)
            i=i+1
    elif ch==3:
        taskno=int(input("Enter the task number to mark as done:"))
        l=list(task)
        a=l[taskno-1]
        task[a]="done"
        print("Task marked as done!")
    elif ch==4:
        break
    else:
        print("Please enter a valid option!")
print("Thank you!")
