import poplib
from email import parser

pop_conn = poplib.POP3_SSL('pop.mail.yahoo.in')
a = raw_input("Enter your yahoo email address: ")
pop_conn.user(a)
b = raw_input("Enter your Pssword: ")
pop_conn.pass_(b)

iMessageCount = len(pop_conn.list()[1])
print iMessageCount

