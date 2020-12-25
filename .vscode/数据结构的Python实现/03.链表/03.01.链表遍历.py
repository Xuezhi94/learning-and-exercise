import sys


#建立链表节点
class student:
    name = ''
    Math = 0
    Eng = 0
    no = ''
    next = None


#建立链表头部
head = student()
head.next = None
ptr = head #指针开始指向链表头部
Msum = Esum = num = student_no = 0
select = 0

while select != 2:
    print('(1)新增 (2)离开')
    try:
        select = int(input('请输入一个选项：'))
    except ValueError:
        print('输入错误')
        print('请重新输入\n')
    if select ==1:
        new_data = student()
        new_data.name = input('姓名：')
        new_data.no = input('学号：')
        new_data.Math = eval(input('数学成绩：'))
        new_data.Eng = eval(input('英语成绩：'))
        new_data.next = None
        ptr.next = new_data #将新节点添加在链表尾部
        ptr = ptr.next #存取指针指向新节点
        num +=1

ptr = head.next
print()
#链表遍历
while ptr != None:
    print('姓名：%s\t 学号：%s\t 数学成绩：%d\t 英语成绩：%d'\
        %(ptr.name,ptr.no,ptr.Math,ptr.Eng))
    Msum += ptr.Math
    Esum += ptr.Eng
    student_no += 1
    ptr = ptr.next

if student_no !=0:
    print('-'*40)
    print('本链表中学生的数学平均成绩为：%.2f 英语平均成绩为：%.2f'\
        %(Msum/student_no,Esum/student_no))

