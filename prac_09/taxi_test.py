from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    print(my_taxi)
    my_taxi.drive(40)
    print(f"{my_taxi}, current fare = ${my_taxi.get_fare()}")
    my_taxi.start_fare()
    print(my_taxi)
    my_taxi.drive(100)
    print(my_taxi)
    print(f"{my_taxi}, current fare = ${my_taxi.get_fare()}")


main()
