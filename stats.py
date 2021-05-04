import database

class statistics:
	def stat(self):
		hall_seat = database.hall_row * database.hall_coloumn
		count = len(database.booked_ticket_seat)
		total_income = sum(database.booked_ticket_price)
		if count == 0:
			percentage = 0
		else:
			percentage = (count/hall_seat)*100
			rounded_off_percentage = round(percentage, 2)

		print('1. Number of purchased tickets: ', count)
		print('2. Percentage of tickets booked: ', rounded_off_percentage, '%')
		print('3. Current income: ', database.current_ticket_price, '$')
		print('4. Total income: ', total_income, '$')
