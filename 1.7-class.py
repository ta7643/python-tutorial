#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("James", 2000)
"This would create second object of Employee class"
emp2 = Employee("Bond", 5000)

# accessing 
emp1.displayEmployee()
emp2.displayEmployee()

# accessing variable of class object direct
print "Total Employee %d" % Employee.empCount

# accessing it over the object
emp1.displayCount()
emp2.displayCount()