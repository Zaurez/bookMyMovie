#Welome message
# print('Hello....!!!')
# print('Welcome to our movie booking portal')
import variable
# print('\nFollow the given menu to proceed further.\n')

import menu
display_menu = menu.menu()
all_list = display_menu.all()
count = True
seat_configured = False

while count == True:
	try:
		# choice = int(input('\nEnter the serial number of your choice from menu: '))
		choice = int(input('\n'))

		#for exit
		if choice == 0:
			count = False
			# print('Thanks for visiting our portal.')
			break;

		# for showing seat
		elif choice == 1:
			if seat_configured == False:
				import seat
				seat_capacity = seat.seat()
				hall = seat_capacity.hall_setup(variable.row,variable.coloumn)
				seat_display = seat_capacity.show_seat(variable.row,variable.coloumn)
				print('\n')
				display_menu.all()
				seat_configured = True
			else:
				import seat
				seat_capacity = seat.seat()
				hall = seat_capacity.hall_setup(variable.row,variable.coloumn)
				seat_booked = seat_capacity.booked_seat()
				print('\n')
				display_menu.all()

			continue

		# Buy a ticket
		elif choice == 2:
			import seat
			import ticket
			import menu
			import database
			import variable
			row_choice = int(input('Desired row number: '))
			coloumn_choice = int(input('Desired coloumn number: '))
			
			book_ticket = ticket.ticket()
			ticket1 = book_ticket.buy_ticket(row_choice, coloumn_choice)
			rule = book_ticket.ticket_rule()
			ticket2 = book_ticket.check_valid_seat()
			ticket3 = book_ticket.seat_confirmation()
			ticket4 = book_ticket.ticket_record()
			ticket5 = book_ticket.record_text_file()
			
			seat_capacity = seat.seat()
			hall = seat_capacity.hall_setup(variable.row,variable.coloumn)
			seat_booked = seat_capacity.booked_seat()
			print('\n')
			display_menu.all()
			continue

		elif choice == 3:
			import stats
			import database
			ticket_stat = stats.statistics()
			book_stat = ticket_stat.stat()
			print('\n')
			display_menu.all()
			continue

		elif choice == 4:
			import user_info
			import database
			ask_row = int(input('Enter the row number to check: '))
			ask_coloumn = int(input('Enter the coloumn number to check: '))
			info = user_info.booked_user()
			info1 = info.input(ask_row, ask_coloumn)
			show_info = info.user_info_dictionary()
			print('\n')
			display_menu.all()
			continue
	except:
		break;
