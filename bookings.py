
from datetime import datetime

properties = [
    {"id": 1, "name": "Studio Apartment", "price": 1500, "available": True},
    {"id": 2, "name": "One Bedroom", "price": 2500, "available": True},
    {"id": 3, "name": "Two Bedroom", "price": 4000, "available": True},
]

bookings = []


def show_properties():
    print("\n--- Available Properties ---")
    for property in properties:
        if property["available"]:
            print(
                f'{property["id"]}. {property["name"]} '
                f'- KSh {property["price"]}/night'
            )


def make_booking():
    show_properties()

    try:
        property_id = int(input("\nEnter property ID: "))
        selected = next(
            (p for p in properties if p["id"] == property_id),
            None
        )

        if not selected or not selected["available"]:
            print("Property not available.")
            return

        customer = input("Enter your name: ").strip()
        if not customer:
            print("Name is required.")
            return

        check_in = input("Check-in date (YYYY-MM-DD): ")
        check_out = input("Check-out date (YYYY-MM-DD): ")

        start = datetime.strptime(check_in, "%Y-%m-%d").date()
        end = datetime.strptime(check_out, "%Y-%m-%d").date()

        if start < datetime.today().date() or end <= start:
            print("Please enter valid future dates.")
            return

        nights = (end - start).days
        total = nights * selected["price"]

        booking = {
            "booking_id": len(bookings) + 1,
            "customer": customer,
            "property": selected["name"],
            "check_in": str(start),
            "check_out": str(end),
            "total": total,
        }

        bookings.append(booking)

        print("\nBooking created successfully!")
        print(f"Booking ID: {booking['booking_id']}")
        print(f"Property: {booking['property']}")
        print(f"Duration: {nights} nights")
        print(f"Total: KSh {total}")

    except ValueError:
        print("Invalid input. Check the property ID and dates.")


def view_bookings():
    print("\n--- All Bookings ---")

    if not bookings:
        print("No bookings yet.")
        return

    for booking in bookings:
        print(booking)


while True:
    print("\n===== RENTAL BOOKING SYSTEM =====")
    print("1. View available properties")
    print("2. Make a booking")
    print("3. View bookings")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_properties()
    elif choice == "2":
        make_booking()
    elif choice == "3":
        view_bookings()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")