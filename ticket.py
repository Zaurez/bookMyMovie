import database
import variable

# row_choice = int(input('Please enter the desired row: '))
# coloumn_choice = int(input('Please enter the desired coloumn: '))

class ticket():
    ticket_booked = []
    # dictionary_record = {}
    valid_seat = False
    ticket_price = 0
    back_row_count = 0
    seat_count = 0
    chosen_row = 0
    chosen_coloumn = 0
    book_status = False
    check_seat_number = ''
    def buy_ticket(self, row_choice, coloumn_choice):
            self.row_choice = row_choice
            self.coloumn_choice = coloumn_choice
            ticket.chosen_row = self.row_choice
            ticket.chosen_coloumn = self.coloumn_choice
            front_row_count = database.hall_row//2
            ticket.back_row_count = database.hall_row - front_row_count
            ticket.seat_count = database.hall_row*database.hall_coloumn
            # print('\nFront row count: ',front_row_count)
            # print('\nBack row count:', ticket.back_row_count)
            # print('\nThe seat count is:', ticket.seat_count)

    # rules for ticket price
    def ticket_rule(self):
            #for hall capacity of 60 seats
            if ticket.seat_count < 61:
                ticket.ticket_price = 10
            
            #for hall capacity of more than 60 seats
            else:
                
                #hall distribution in Front and Back Row
#             if database.hall_row % 2 ==0:
                if ticket.chosen_row > ticket.back_row_count:
                    ticket.ticket_price = 10
                else:
                    ticket.ticket_price = 8
#             else:
#                 if ticket.chosen_row >= ticket.back_row_count:
#                     ticket.ticket_price = 10
#                 else:
#                     ticket.ticket_price = 8

    def check_valid_seat(self):
            #checking if seat is valid for given hall
            if ticket.chosen_row > database.hall_row:
                print('This row is not available in hall.')
                ticket.valid_seat = False
            else:
                if ticket.chosen_coloumn > database.hall_coloumn:
                    print('This seat is not a valid seat for this row.')
                    ticket.valid_seat = False
                else:
                    # checking if seat is available or not
                    ticket.check_seat_number = int(str(ticket.chosen_row) + str(ticket.chosen_coloumn))
                    if ticket.check_seat_number in database.booked_ticket_seat: #check 1
                        print('The seat is already booked.')
                        ticket.valid_seat = False
                    elif ticket.check_seat_number in ticket.ticket_booked: #check 2 
                        print('This seat is already booked. You can try for another.')
                        ticket.valid_seat = False
                    else:
                        ticket.valid_seat = True
                        print('\nThe ticket price is: ',ticket.ticket_price, '$\n')

    def seat_confirmation(self):
            if ticket.valid_seat == True:
                confirmation_input = input('Please press Y to confirm or N to cancel: ')
                if confirmation_input in ['Y','y']:
                    database.current_ticket_price = ticket.ticket_price
                    database.booked_ticket_price.append(ticket.ticket_price)
                    database.name = input('Name: ')
                    count_gender = 3
                    while count_gender != 1:
                        try:
                            database.gender = input('Gender: Press M for Male and F for Female: ')
                            if database.gender not in ['M','m','F','f']:
                                print('\nPlease enter valid input. Press M for Male and F for Female: ')
                                count_gender = count_gender - 1
                                print('Attemps left for input: ', count_gender)
                            else:
                                break;
                        except:
                            continue
                    else:
                        ('No more attempts left.')

                    database.age = int(input('Age: '))

                    count_phone = 3
                    while count_phone != 0:
                        try:
                            database.phone = int(input('Phone no: '))
                            if len(str(database.phone)) != 10:
                                print("\nPlease enter valid input. Phone number should be 10 digits. Don't use +91 or 0 as prefix: ")
                                count_age = count_age - 1
                                print('Attemps left for input: ', count_phone)
                            else:
                                break;
                        except:
                            continue
                    else:
                        ('No more attempts left.')
                    ticket.book_status = True
                    # print('Ticket booked successfully for seat: ', ticket.check_seat_number)
                    print('Ticket booked successfully')
                else:
                    print('The ticket booking has been cancelled by the user')
            else:
                pass


    def ticket_record(self):
                if ticket.valid_seat == True and ticket.book_status == True:
                    
                    #storing seat numberin module database's variable
                    database.seat_number = 'R' + str(ticket.chosen_row) + 'C' + str(ticket.chosen_coloumn)
                    
                    current_ticket = int(str(ticket.chosen_row) +  str(ticket.chosen_coloumn))
                    # print('Current booked ticket is: ', current_ticket)
                    
                    #saving current ticket number to database variable
                    database.booked_ticket_seat.append(current_ticket)
                    
                    #saving current_ticket number to class variable
                    ticket.ticket_booked.append(current_ticket)
                    # print('Booked ticket is: ', database.booked_ticket_seat)

                    #saving row and coloumn of booked ticket to database variable
                    database.booked_ticket_x_list.append(ticket.chosen_row)
                    database.booked_ticket_y_list.append(ticket.chosen_coloumn)

                    #debugging for booked row and coloumn
                    # print('x: ',database.booked_ticket_x_list)
                    # print('y: ',database.booked_ticket_y_list)

                    #saving booked info in database dictionary variable
                    database.dictionary_record[database.seat_number] = {'Name': database.name, 'Gender': database.gender, 'Age': database.age, 'Ticket Price': str(database.current_ticket_price) + '$', 'Phone No:':database.phone}
                    # print(database.dictionary_record)

    def record_text_file(self):
                #saving user info in text file...
                f = open('booked_ticket.txt', 'a')
                f.write('\n')
                f.write('The user detail for seat: '+ database.seat_number)
                f.write('\nName: ' + database.name)
                f.write('\nGender: ' + database.gender)
                f.write('\nAge: ' + str(database.age))
                f.write('\nTicekt Price: ' + str(database.current_ticket_price))
                f.write('\nPhone No: '+ str(database.phone))
                f.close()
                
# book_ticket = ticket()
# ticket1 = book_ticket.buy_ticket(row_choice, coloumn_choice)
# rule = book_ticket.ticket_rule()
# ticket2 = book_ticket.check_valid_seat()
# ticket3 = book_ticket.seat_confirmation()
# ticket4 = book_ticket.ticket_record()
# ticket5 = book_ticket.record_text_file()


    
