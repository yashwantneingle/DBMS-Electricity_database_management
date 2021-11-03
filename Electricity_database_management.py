from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host="localhost",user="root",password="yashwant",database="Electricity")
cursor = conn.cursor()

class GUI(Tk):
	def __init__(self):
		Tk.__init__(self)
		self._frame = None
		self.title(" Electricity Management system ")
		self.switch(Management_Portal)
		self.geometry('800x800')
		self.config(bg = "light green")

	def switch(self, frame_class,list=[]):
		"""Destroys current frame and replaces it with a chosen by the user"""
		new_frame = frame_class(self,list)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()
class Management_Portal(Frame):
	"""Menu bar to select login role"""
	def __init__(self, master,role):
		
		Frame.__init__(self, master)
		

		self.config(bg = "light green")
		"""Frame widgets"""
		label = Label(self, font = ('elephant',(20)),text = "Electricity Management system !\n", bg = "light green", fg = "black")
		label.pack(padx = 10, pady = 20)

		button = Button(self, text = "Login as Admin",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Login,["Admin"]))
		button.pack(padx = 10, pady = 10)
		button2 = Button(self, text = "Login as Customer",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Login,["Customer"]))
		button2.pack(padx = 10, pady = 10)
		button3 = Button(self, text = "Login as Employee",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Login,["Employee"]))
		button3.pack(padx = 10, pady = 10)	
		button4 = Button(self, text = "Exit menu",font = ('Times new roman',(30)),bg = "white", width = 20, command = self.leave)
		button4.pack(padx = 10, pady = 10)
		
	def leave(self):
		"""Close the GUI Application"""
		self.destroy()
		exit()
class Login(Frame):
	def __init__(self, master,list):
		role = list[0]
		
		
		Frame.__init__(self, master)
		self.config(bg = "light green")
		
		def on_click():
			"""Storing input"""
			user_id = entryUser.get()
			user_pass = entryPass.get()
			user_region = entry_region.get()
			entryUser.delete(0,END)
			entryPass.delete(0,END)
			entry_region.delete(0,END)
			try :
				query = f"Select password from {role} where id = \"{user_id}\" AND Region_id = \"{user_region}\""
				cursor.execute(query)
				result = cursor.fetchall()
				if result == []:
					messagebox.showerror("Error", "Please enter correct data!")
				else:
					password = result[0][0]
					if password == user_pass:
						if role == "Customer":
							master.switch(Customer,[user_id,user_region])
						elif role == "Admin":
							master.switch(Admin,[user_id,user_region])
						elif role == "Employee":
							master.switch(Employee,[user_id,user_region])
					else :
						messagebox.showerror("Error", "Please enter correct data!")
			except:
				messagebox.showerror("Error", "Please enter correct data!")
		"""Labels for window"""
		label = Label(self, text ="Enter the Details  ",font = ('Elephant',(20)), bg = "light green", fg = "black")
		label.pack(padx = 10, pady = 60)
		# user input, product
		label2 = Label(self, text = "User_id: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
		label2.pack()
		entryUser = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryUser.pack(padx = 10, pady =10)
		
		label3 = Label(self, text = "Password: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
		label3.pack()
		entryPass = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryPass.pack(padx = 10, pady =5)
		label4 = Label(self, text = "Region id: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
		label4.pack()
		entry_region = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entry_region.pack(padx = 10, pady =5)
		login = Button(self, text = "Login",font = ('times new roman',(25)), width = 8, command = on_click)
		login.pack(padx = 10, pady = 10)
		forgot = Button(self, text = "Forgot password",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Forget,[role]))
		forgot.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Management_Portal))
		self.button.pack(padx = 10, pady = 10)
class Forget(Frame):
               def __init__(self, master,list):
                              role = list[0]
                              Frame.__init__(self, master)
                              self.config(bg = "light green")
                              def check():
                                             """Storing input"""
                                             a = int(e1.get())
                                             b = int(e2.get())
                                             e1.delete(0,END)
                                             e2.delete(0,END)
                                             query = f"Select * from {role} where id = \"{a}\" AND Region_id = \"{b}\""
                                             cursor.execute(query)
                                             result = cursor.fetchall()
                                             if result == []:
                                                      messagebox.showerror("Error", "Customer doesn't exist")
                                             else:
                                                      self.button = Button(self, text = "Change Password",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Change_Password,[role,a,b]))
                                                      self.button.pack(padx = 50, pady = 50, side = BOTTOM)
			
                              label1 = Label(self, text = "ID: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                              label1.pack()
                              e1 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                              e1.pack(padx = 10, pady =10)
                              label2 = Label(self, text = "Region_id: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                              label2.pack()
                              e2 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                              e2.pack(padx = 10, pady =10)
                              self.check = Button(self, text = "Check user",font = ('times new roman',(20)), width = 12, command = check)
                              self.check.pack(padx = 50, pady = 50, side = BOTTOM)
                              self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Management_Portal))
                              self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Change_Password(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             role = list[0]
                             region_id = list[2]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             def change_pass():
                                      new = name.get()
                                      query = f"UPDATE {role} SET password=\"{new}\" where id = \"{user_id}\" AND Region_id = \"{region_id}\""
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Management_Portal))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label = Label(self, text = "New Password: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label.pack()
                             name = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             name.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = change_pass)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Management_Portal))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
		
		
class Customer(Frame):
	def __init__(self, master,list):
		
		user_id = list[0]
		region_id = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light green")
		
		query = f"Select * from Customer where id = \"{user_id}\" AND Region_id = \"{region_id}\""
		cursor.execute(query)
		result = cursor.fetchall()
		response = f" \n\nCustomer ID : {result[0][0]} \nRegion_id : {result[0][1]} \nName : {result[0][2]} \nEmail_id : {result[0][3]} \nMobile_no : {result[0][4]} \nPassword : {result[0][5]} \nAddress : {result[0][7]}"
		details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		
		details.configure(state ='normal')
		details.insert(END,response)
		details.configure(state ='disabled')
		details.pack(padx = 10 , pady = 10, anchor = 'w')
		
		self.Edit = Button(self, text = "Edit Customer info ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
		self.Edit.pack(padx = 30, pady = 10,side = LEFT)
		complain = Button(self, text = "Raise Complaint ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Raise_complaint,[Customer,user_id,region_id]))
		complain.pack(padx = 10, pady = 10,side = LEFT)
		
		Transaction = Button(self, text = "Transaction",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(transaction,[Customer,user_id,region_id]))
		Transaction.pack(padx = 30, pady = 10, side = LEFT)
		Bill = Button(self, text = "View Bill",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Billing,[Customer,user_id,region_id]))
		Bill.pack(padx = 30, pady = 20, side = LEFT)
		password = Button(self, text = "Change Password",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Change_Password,["Customer",user_id,region_id]))
		password.pack(padx = 30, pady = 20, side = LEFT)
		self.button = Button(self, text = "Logout",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Management_Portal))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
class Edit_details(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             region_id = list[2]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             name = Button(self, text = "Edit name ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_name,[Customer,user_id,"Customer",region_id]))
                             name.pack(padx = 30, pady = 10,side = LEFT)
                             mobile = Button(self, text = "Edit mobile no ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_mobile_no,[Customer,user_id,"Customer",region_id]))
                             mobile.pack(padx = 30, pady = 10,side = LEFT)
                             email = Button(self, text = "Edit email_id ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_email,[Customer,user_id,"Customer",region_id]))
                             email.pack(padx = 30, pady = 10,side = LEFT)
                             address = Button(self, text = "Edit Address ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_address,[Customer,user_id,"Customer",region_id]))
                             address.pack(padx = 30, pady = 10,side = LEFT)
                             self.back = Button(self, text = "Back to login",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Customer,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Edit_name(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             role = list[2]
                             region_id = list[3]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             def change_name():
                                      new = name.get()
                                      print(new)
                                      query = f"UPDATE {role} SET name=\"{new}\" where id = \"{user_id}\" AND Region_id = \"{region_id}\""
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label = Label(self, text = "Name: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label.pack()
                             name = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             name.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = change_name)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Edit_mobile_no(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             role = list[2]
                             region_id = list[3]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             def change_mobile():
                                      new = int(mobile.get())
                                      query = f"UPDATE {role} SET phone=\"{new}\" where id = \"{user_id}\" AND Region_id = \"{region_id}\""
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label = Label(self, text = "New mobile no: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label.pack()
                             mobile = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             mobile.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = change_mobile)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Edit_email(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             role = list[2]
                             region_id = list[3]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             def change_email():
                                      new = email.get()
                                      query = f"UPDATE {role} SET email_id=\"{new}\" where id = \"{user_id}\" AND Region_id = \"{region_id}\""
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label = Label(self, text = "New email id: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label.pack()
                             email = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             email.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = change_email)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Edit_address(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             role = list[2]
                             region_id = list[3]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             def change_address():
                                      new = add.get()
                                      query = f"UPDATE {role} SET address=\"{new}\" where id = \"{user_id}\" AND Region_id = \"{region_id}\""
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label = Label(self, text = "Address: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label.pack()
                             add = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             add.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = change_address)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Edit_details,[Customer,user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)

class transaction(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             region_id = list[2]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             query = f"Select * from transaction where id = \"{user_id}\" AND Region_id = \"{region_id}\""
                             cursor.execute(query)
                             result = cursor.fetchall()
                             if result == []:
                                       messagebox.showerror("Error", "No transaction history found")
                             else:
                                       details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
                                       response = f" \n\nCustomer ID : {result[0][0]} \nRegion_id : {result[0][1]} \nPaid_amount : {result[0][2]} \nDate of transaction : {result[0][3]} \nStatus : {result[0][4]} \n"
                                       details.configure(state ='normal')
                                       details.insert(END,response)
                                       details.configure(state ='disabled')
                                       details.pack(padx = 10 , pady = 10, anchor = 'w')
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Customer,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Billing(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             region_id = list[2]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             query = f"Select * from Billing where id = \"{user_id}\" AND Region_id = \"{region_id}\""
                             cursor.execute(query)
                             result = cursor.fetchall()
                             details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
                             amount = str(float(result[0][3]))
                             date = str(result[0][5])
                             response = "Customer_id :"+ str(result[0][0]) + "\n" + "Region_id :" + str(result[0][1]) + "\n" + "Units_Consumed :" + str(result[0][2]) + "\n" + "Amount :" + amount + "\n" + "Due date : " + date + "\n"
                             details.configure(state ='normal')
                             details.insert(END,response)
                             details.configure(state ='disabled')
                             details.pack(padx = 10 , pady = 10, anchor = 'w')
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Customer,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Raise_complaint(Frame):
               def __init__(self, master,list):
                             user_id = list[1]
                             region_id = list[2]
                             Frame.__init__(self,master)
                             self.config(bg = "light green")
                             def fill_complaint():
                                      res = compl.get()
                                      id = user_id
                                      d = "NOT PROCESSED"
                                      query = f"Insert into `complaint` VALUES(\"{user_id}\" ,\"{region_id}\", \"{res}\", \"{d}\")"
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Customer,[user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label = Label(self, text = "Name: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label.pack()
                             compl = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             compl.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = fill_complaint)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Customer,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Employee(Frame):
	def __init__(self, master,list):
		
		user_id = list[0]
		region_id = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light green")
		query = f"Select * from Employee where id = \"{user_id}\" AND Region_id = \"{region_id}\""
		cursor.execute(query)
		result = cursor.fetchall()
		message = "Emp_ID :" + str(result[0][0]) + "\n" + "Region_id :" + str(result[0][1]) + "\n" + "Name :" + result[0][2] + "\n" + "Email_id :" + str(result[0][3]) + "\n" + "Mobile no: " + str(result[0][4]) + "\n" + "Password :" + result[0][5] + "\n"
		label = Label(self, text ="Employee Details  ",font = ('Elephant',(30)), bg = "light green", fg = "black")
		label.pack(padx = 10, pady = 60)
		details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		details.pack(padx = 20 , pady = 20, anchor = 'w')
		
		details.configure(state ='normal')
		details.insert(END,message)
		details.configure(state ='disabled')
		query = Button(self, text = "Manage Customer queries",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Manage_queries,[user_id,region_id]))
		query.pack(padx = 30, pady = 10,side = LEFT)
		#approve_bill = Button(self, text = "Approve bills",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
		#approve_bill.pack(padx = 10, pady = 10,side = LEFT)
		self.button = Button(self, text = "Logout",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Management_Portal))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
class Manage_queries(Frame):
	def __init__(self, master,list):
		region_id = list[1]
		user_id = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light green")		             
		                       
		query = f"Select * from complaint where Region_id = \"{region_id}\""
		cursor.execute(query)
		result = cursor.fetchall()
		if result == []:
		         messagebox.showerror("Error", "No queries found")
		else:
		         message = ''
		         for i in range(len(result)):
		                m = str(result[i][0]) + ' '  + str(result[i][1]) + ' ' + result[i][2] + ' ' + result[i][3]
		                message = message + m + "\n"
		         label = Label(self, text ="Employee Details  ",font = ('Elephant',(30)), bg = "light green", fg = "black")
		         label.pack(padx = 10, pady = 60)
		         details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		         details.pack(padx = 20 , pady = 20, anchor = 'w')
		         details.configure(state ='normal')
		         details.insert(END,message)
		         details.configure(state ='disabled')
		         action = Button(self, text = "Give response",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(give_response,[user_id,region_id]))
		         action.pack(padx = 50, pady = 50, side = BOTTOM)
		self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Employee,[user_id,region_id]))
		self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class give_response(Frame):
               def __init__(self, master,list):
                             user_id = list[0]
                             region_id = list[1]
                             Frame.__init__(self,master)
                             self.config(bg = "yellow")
                             def take_action():
                                      id = int(e1.get())
                                      res = e2.get()
                                      query = f"UPDATE complaint SET response=\"{res}\" where id = \"{id}\" AND Region_id = \"{region_id}\""
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Employee,[user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label1 = Label(self, text = "Customer id: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label1.pack()
                             e1 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e1.pack(padx = 10, pady =10)
                             label2 = Label(self, text = "response: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label2.pack()
                             e2 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e2.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = take_action)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Employee,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Admin(Frame):
	def __init__(self, master,list):
		
		user_id = list[0]
		region_id = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light green")
		query = f"Select * from Admin where id = \"{user_id}\" AND Region_id = \"{region_id}\""
		cursor.execute(query)
		result = cursor.fetchall()
		message = "ID :" + str(result[0][0]) + "\n" + "Region_id :" + str(result[0][1]) + "\n" + "Name :" + result[0][2] + "\n" + "Email_id :" + str(result[0][3]) + "\n" + "Password :" + result[0][4] + "\n"
		label = Label(self, text ="Admin Details  ",font = ('Elephant',(30)), bg = "light green", fg = "black")
		label.pack(padx = 10, pady = 60)
		details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		details.pack(padx = 10 , pady = 10, anchor = 'w')
		
		details.configure(state ='normal')
		details.insert(END,message)
		details.configure(state ='disabled')
		region_id = result[0][1]
		#Edit = Button(self, text = "Edit Profile ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_Profile,["Admin",user]))
		#Edit.pack(padx = 30, pady = 10,side = LEFT)
		Manages = Button(self, text = "Manages data",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
		Manages.pack(padx = 10, pady = 10,side = LEFT)
		self.button = Button(self, text = "Logout",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Management_Portal))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
class Admin_manager(Frame):
               def __init__(self, master,list):
                             user_id = list[0]
                             region_id = list[1]
                             Frame.__init__(self,master)
                             self.config(bg = "yellow")
                             self.add = Button(self, text = "Add new Customer",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Add_customer,[user_id,region_id]))
                             self.add.pack(padx = 90, pady = 60, side = BOTTOM)
                             self.delete = Button(self, text = "Delete Customer data",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Delete_customer,[user_id,region_id]))
                             self.delete.pack(padx = 90, pady = 60, side = BOTTOM)
                             self.unit = Button(self, text = "Set unit rates",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Set_unit_rate,[user_id,region_id]))
                             self.unit.pack(padx = 50, pady = 50, side = BOTTOM)
                             self.back = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Admin,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Set_unit_rate(Frame):
               def __init__(self, master,list):
                             user_id = list[0]
                             region_id = list[1]
                             Frame.__init__(self,master)
                             self.config(bg = "yellow")
                             def set_rate():
                                      a = int(e1.get())
                                      b = int(e2.get())
                                      c = int(e3.get())
                                      d = e4.get()
                                      query = f"Insert into `Units_Rate` VALUES(\"{d}\" ,\"{region_id}\", \"{a}\", \"{b}\",\"{c}\")"
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label1 = Label(self, text = "For twohundred+: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label1.pack()
                             e1 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e1.pack(padx = 10, pady =10)
                             label2 = Label(self, text = "For fivehundred+: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label2.pack()
                             e2 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e2.pack(padx = 10, pady =10)
                             label3 = Label(self, text = "For thousand+: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label3.pack()
                             e3 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e3.pack(padx = 10, pady =10)
                             label4 = Label(self, text = "Month: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label4.pack()
                             e4 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e4.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = set_rate)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Add_customer(Frame):
               def __init__(self, master,list):
                             user_id = list[0]
                             region_id = list[1]
                             Frame.__init__(self,master)
                             self.config(bg = "yellow")
                             def add():
                                      a = int(e1.get())
                                      c = e3.get()
                                      d = e4.get()
                                      e = int(e5.get())
                                      f = e6.get()
                                      g = e7.get()
                                      h = e8.get()
                                      query = f"Insert into `Customer` VALUES(\"{a}\", \"{region_id}\",\"{c}\",\"{d}\",\"{e}\",\"{f}\",\"{h}\",\"{g}\")"
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label1 = Label(self, text = "ID: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label1.pack()
                             e1 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e1.pack(padx = 10, pady =10)
                             label3 = Label(self, text = "Name: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label3.pack()
                             e3 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e3.pack(padx = 10, pady =10)
                             label4 = Label(self, text = "Email_id: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label4.pack()
                             e4 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e4.pack(padx = 10, pady =10)
                             label5 = Label(self, text = "Mobile_no(10 digits only): ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label5.pack()
                             e5 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e5.pack(padx = 10, pady =10)
                             label6 = Label(self, text = "Password: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label6.pack()
                             e6 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e6.pack(padx = 10, pady =10)
                             label7 = Label(self, text = "Address: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label7.pack()
                             e7 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e7.pack(padx = 10, pady =10)
                             label8 = Label(self, text = "DOB: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label8.pack()
                             e8 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e8.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = add)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
class Delete_customer(Frame):
               def __init__(self, master,list):
                             user_id = list[0]
                             region_id = list[1]
                             Frame.__init__(self,master)
                             self.config(bg = "yellow")
                             def delete():
                                      a = int(e1.get())
                                      b = int(e2.get())
                                      query = f"Delete from `Customer` where id=\"{a}\" AND Region_id=\"{b}\""
                                      cursor.execute(query)
                                      conn.commit()
                                      self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
                                      self.back.pack(padx = 50, pady = 50, side = BOTTOM)
                                      
                             label1 = Label(self, text = "ID: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label1.pack()
                             e1 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e1.pack(padx = 10, pady =10)
                             label2 = Label(self, text = "Region_id: ",font = ('times new roman',(25)), bg = "light green", fg = "black")
                             label2.pack()
                             e2 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
                             e2.pack(padx = 10, pady =10)
                             submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 12, command = delete)
                             submit.pack(padx = 50, pady = 50, side = LEFT)
                             self.back = Button(self, text = "Back to manager",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Admin_manager,[user_id,region_id]))
                             self.back.pack(padx = 50, pady = 50, side = BOTTOM)
if __name__ == "__main__":
    app = GUI()
    app.mainloop()
    cursor.execute("SHOW TABLES")
    for i in cursor:
        print(i)
