class job:
    def __init__(self,role,location,salary):
        self.role = role
        self.location = location
        self.salary = salary
    def info(self):
        return '{} {} {}'.format(self.role,self.location,self.salary)
    @classmethod
    def clsfun(cls):
        pass


class company(job):
    pass


sidjob = company('bre','cali',145000)

print(company.info(sidjob))
print(isinstance(sidjob,job))
print(issubclass(company,job))
