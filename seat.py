
import database
class seat():
	
	def hall_setup(self,row,coloumn):
		self.row = row
		self.coloumn = coloumn
		print('\nCinema: ')
		# print('The sitting capacity of hall is: ', self.row*self.coloumn, '\n')

	def show_seat(self,row,coloumn):
		for x in range(0, self.row + 1):
		    if x == 0:
		        row_string = ' ' + ' '
		    else:
		        row_string = str(x) + ' '
		    for y in range(1,self.coloumn + 1):
		        if x == 0:
		            row_string = row_string + str(y) + ' '
		        else:
		            row_string = row_string + 'S' + ' '
		    print(row_string)

	def booked_seat(self):
		for x in range(0, database.hall_row + 1):
			if x == 0:
				row_string = ' ' + ' '
			else:
				row_string = str(x) + ' '
			for y in range(1,database.hall_coloumn + 1):
				if x == 0:
					row_string = row_string + str(y) + ' '
				elif x in database.booked_ticket_x_list:
					if y in database.booked_ticket_y_list:
						row_string = row_string + 'B'  + ' '
					else:
						row_string = row_string + 'S' + ' '
				else:
					row_string = row_string + 'S' + ' '
			print(row_string)



