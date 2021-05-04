import database

#inputs for individual module checking....
# ask_row = int(input('Enter the row number to check: '))
# ask_coloumn = int(input('Enter the coloumn number to check: '))

class booked_user:
	check_seat_number = ''
	row_asked = 0
	coloumn_asked = 0
	def input(self, ask_row, ask_coloumn):
		self.ask_row = ask_row
		self.ask_coloumn = ask_coloumn
		booked_user.row_asked = ask_row
		booked_user.coloumn_asked = ask_coloumn
		booked_user.check_seat_number = 'R' + str(booked_user.row_asked) + 'C' + str(booked_user.coloumn_asked)
		# print(booked_user.check_seat_number)

	def user_info_text_file(self):
		print(booked_user.check_seat_number)
		print(database.dictionary_record)
		line_count = 0
		match_line_number = 0

		with open('booked_ticket.txt', 'r') as read_obj:
			for line in read_obj:
				line_count = line_count + 1
				if booked_user.check_seat_number in line:
					match_line_number = line_count
					# print(match_line_number)
					print(line.rstrip())
					for number in range (match_line_number, match_line_number+4):
						print(next(read_obj).rstrip())
		
		if match_line_number == 0:
			print('The seat is not booked yet...!!!')

	def user_info_dictionary(self):
		#another code from dictionary
		# print(database.dictionary_record)
		for key in database.dictionary_record:
			if key == booked_user.check_seat_number:
				print(' ')
				for sub_key in database.dictionary_record[key]:
					# print(sub_key)
					print(sub_key + ' : ' + str(database.dictionary_record[key][sub_key]))
				break
		else:
			print('\nNot booked yet...!!!')
			
# For module checking....
# info = booked_user()
# info1 = info.input(ask_row, ask_coloumn)
# info2 = info.user_info_dictionary()
