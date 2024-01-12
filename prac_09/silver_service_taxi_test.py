from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2.0)
    print(my_silver_service_taxi)
    my_silver_service_taxi.drive(18)
    print(f"Taxi fare: ${my_silver_service_taxi.get_fare():.2f}")


main()
