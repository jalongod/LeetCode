
# Employee info


class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    # 暴力
    def getImportance2(self, employees, id):
        if len(employees) == 0:
            return 0
        for i in range(len(employees)):
            if employees[i].id == id:
                sum = employees[i].importance
                for subId in employees[i].subordinates:
                    sum += self.getImportance(employees, subId)
                return sum
        return 0

    # dic 
    def getImportance3(self, employees, id):
        if len(employees) == 0:
            return 0
        dic = dict()

        for emp in employees:
            dic.setdefault(emp.id, emp)
        
        return self.getImp(dic, id)
        
    def getImp(self, dic, id):
        if not dic.__contains__(id):
            return 0
        theEmp = dic.get(id)
        sum = theEmp.importance
        for subId in theEmp.subordinates:
            if dic.__contains__(subId):
                sum += self.getImp(dic, subId)
        return sum
        


if __name__ == '__main__':
    sol = Solution()
    emp1 = Employee(1,5,[2,3])
    emp2 = Employee(2,3,[4])
    emp3 = Employee(3,4,[])
    emp4 = Employee(4,1,[])

    max = sol.getImportance([emp1,emp2,emp3,emp4],1)

    print(max)

