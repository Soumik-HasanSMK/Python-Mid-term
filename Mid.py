class Star_Cinema:
    hall_list = []

    def entry_hall(self,ob1):
        self.hall_list.append(ob1)


class Hall:

    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no 

    def entry_show(self, id, movie_name, time):
        info=(id, movie_name, time)
        self.show_list.append(info)

        seat = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = seat

    def book_seats(self, id, row, col):
        if row >= self.rows or row < 0 or col >= self.cols or col < 0:
            print("\tInvalid Seat Number")
        elif self.seats[id][row][col]==1:
            print('\tAlready booked')
        else:
            self.seats[id][row][col]=1
            print(f'\tSeat ({row},{col}) is booked for Show {id}.')
        

    def view_show_list(self):
        for show in self.show_list:
            print(f'Show ID : {show[0]}, Movie Name : {show[1]}, Time : {show[2]}')
    

    def view_available_seats(self,id):
        if id not in self.seats:
            print("Invalid Show ID.")
        
        else:
            print(f'Available seat for {id} :')
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[id][i][j]==0:
                        print('0', end=' ')
                    else:
                        print('x', end=' ')
                print()


cinema = Hall(6,6,1)
cinema.entry_show(101, "Avengers", "1:00pm")
cinema.entry_show(102, "Avatar", "5:00pm ")
cinema.entry_show(103, "Titanic", "9:00pm ")

run=True
while run:
    
    print("\n1. View all shows today")
    print("2. View available seats")
    print("3. Book Ticket")
    print("4. Exit")

    Option=int(input("Enter option : "))

    if Option==1:
        cinema.view_show_list()

    elif Option==2:
        show_id=int(input("Enter Show ID : "))
        cinema.view_available_seats(show_id)

    elif Option==3:
        show_id=int(input("Enter Show ID : "))
        for id in cinema.show_list:
            if id[0] == show_id:
                num_tic=int(input("How many seat you want to book? : "))
                for i in range(num_tic):
                    row=int(input("Enter seat row : "))
                    col=int(input("Enter seat col : "))
                    cinema.book_seats(show_id,row,col)
                break
        else:
            print("\tInvalid Show ID")
    
    elif Option==4:
        run=False

    else:
        print("Invalid option. Please select a right option.")
