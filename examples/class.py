class person(object):
  def __init__(self,first,last,year):
    self.first = first
    self.last  = last
    self.year  = year
    
  def full_name(self):
    return(self.first + ' ' + self.last)
    
  def year_started(self):
    return(self.year)
    
  def __str__(self):
    return("%s %s started in %d" % 
        (self.first,self.last,self.year) )

class employee(person):
  def __init__(self,first,last,year,company):
    person.__init__(self,first,last,year)
    self.companyname = company

  def __str__(self):
    return("%s %s started at %s in %d" % 
    (self.first,self.last,self.companyname,self.year) )
        
  def company(self):
    return(self.companyname)

    
if __name__ == '__main__':
  joe = person('Joe','Pekarek',1994)
  ted = employee('Ted','Miracco',1997,'AWR')
  print type(joe)
  print type(ted)

  print joe
  print ted.year_started()
  print ted.full_name()
  print ted
  print ted.companyname # company property hides company method
  print ted.company()
  
  
  
  

    