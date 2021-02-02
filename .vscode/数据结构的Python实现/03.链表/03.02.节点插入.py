import sys


class Employee(object):
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None

def linked_list_print(head):
    ptr = head
    print('\t员工编号  姓名\t薪水')
    while ptr != None:
        print('\t[%4d]\t%-7s\t$%5d'%(ptr.num,ptr.name,ptr.salary))
        ptr = ptr.next

def find_node(head,position):
    #寻找num属性为position的节点，若不存在返回None
    ptr = head 
    while ptr != None:
        if ptr.num == position:
            return ptr
        ptr = ptr.next
    return ptr

def insert_node(head,ptr,num,salary,name):
    #链表表头head,在ptr所指节点后插入新节点，节点属性值为num,salary,name,
    #若ptr为空则新节点做为表头
    insertnode = Employee()
    if not insertnode :
        return None
    insertnode.num = num
    insertnode.salary = salary
    insertnode.name = name
    insertnode.next = None
    if ptr == None:
        #插入第一个节点
        insertnode.next = head
        return insertnode
    elif ptr.next == None:
        #插入最后一个节点
        ptr.next = insertnode
    else:
        #插入中间节点
        insertnode.next = ptr.next
        ptr.next = insertnode
    return head

position = 0
data = [
    [1001,32367],[1002,24388],[1003,27556],[1007,31299],\
        [1012,42660],[1014,25676],[1018,44145],[1043,52182],\
            [1031,32769],[1037,21100],[1041,32196],[1042,25776]
]
namedata = ['Allen','Scott','Marry','John','Mark','Ricky',\
    'Lisa','Jasica','Hanson','Amy','Bob','Jack']
print(('%s %s'%('员工编号','薪水')+'\t')*4)
print('-'*50)
for i in range(3):
    for j in range(4):
        print('[%4d]\t $%5d\t'%(data[j*3+i][0],data[j*3+i][1]),end='')
    print()
print('-'*50)

#建立员工数据链表
head = Employee()  #建立表头
if not head:
    print('Error!! 内存分配失败！！')
    sys.exit(1)
head.next = None
head.num = data[0][0]
head.salary = data[0][1]
head.name = namedata[0]
ptr = head
#建立链表
for i in range(1,12):
    newnode = Employee()
    if not newnode:
        print('Error!! 内存分配失败！！')
        sys.exit(1)
    newnode.next = None
    newnode.num = data[i][0]
    newnode.salary = data[i][1]
    newnode.name = namedata[i]
    ptr.next = newnode
    ptr = ptr.next
    
while(True):
    print('请输入要插入其后的员工编号，如输入的编号不在此链表中，')
    position = int(input('新输入的员工节点将被作为此链表的头部节点，要结束节点插入过程，请输入-1：'))
    if position == -1:
        break
    else:
        ptr = find_node(head,position)
        new_num = int(input('请输入新插入的员工编号：'))
        new_salary = int(input('请输入此员工的薪水：'))
        new_name = input('请输入此员工的姓名：')
        head = insert_node(head,ptr,new_num,new_salary,new_name)
    print()

linked_list_print(head)


     
    