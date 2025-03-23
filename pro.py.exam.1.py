#Initialize Variables
net_sal = 0
m_gross_sal = 0
sal_scale = 0
rem = 0

#Take the input from the user
m_gross_sal = float(input("Enter your Monthly Gross Salary = "))


#Calculate the tax and the salary scale as well

if  m_gross_sal < 100_000 :
    rem = m_gross_sal * 0
    sal_scale = m_gross_sal + rem

elif m_gross_sal <= 150_000 :
    rem =  (m_gross_sal - 100_000 ) * 0.05
    sal_scale = m_gross_sal + rem

elif m_gross_sal <= 250_000 :
    rem = ((m_gross_sal -  150_000) * 0.1)
    sal_scale = m_gross_sal + rem + 5000

else:
    rem = ((m_gross_sal - 250_000) * 0.12)
    sal_scale = m_gross_sal + rem + 15000 

#Show the result to the user
print("Your Salary Scale is " ,sal_scale)

