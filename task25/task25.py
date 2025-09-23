my_list = [1,4,6,7,8]
target = 5

for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] + my_list[j] == target:
            print({i + 1, j + 1})

            # time complexcity is 0(n*2)

class Movie:
    def __init__(self, movie_name, movie_id, available_seats, price_per_ticket):
        self.movie_name = movie_name
        self.movie_id = movie_id
        self.available_seats = available_seats
        self.price_per_ticket = price_per_ticket

class Cinemahall:
    def __init__(self):
        self.movies = {}
        self.total_rev = 0

    def add_movie(self, movie):
        self.movies[movie.movie_id] = movie

    def book_ticket(self, movie_id, num_tickets):
        if num_tickets <= 0:
            print("Booking should be unsuccessful")
            return None

        if movie_id in self.movies:
            movie = self.movies[movie_id]
          
            if movie.available_seats >= num_tickets:
                movie.available_seats -= num_tickets
                cost = num_tickets * movie.price_per_ticket
                self.total_rev += cost
                print("Booking successful")
                print("Seats left now:", movie.available_seats)
                return cost  
            else:
                print("House full")
                return None   
        else:
            print("Movie not found ")
            return None

    def get_total_rev(self):
        return self.total_rev


movie1 = Movie("Fast and Furious", 1, 10, 100)
movie2 = Movie("Conjuring", 2, 10, 100)

cinema = Cinemahall()  
cinema.add_movie(movie1)
cinema.add_movie(movie2)

cost1 = cinema.book_ticket(1, 2)
print("Cost:", cost1)

cost2 = cinema.book_ticket(2, 3)
print("Cost:", cost2)
print("Total Rev:", cinema.get_total_rev())




    

    




