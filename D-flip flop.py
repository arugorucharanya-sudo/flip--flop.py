# D Flip-Flop Calculator and Simulator
# Digital Circuits / Electrical Engineering
#
# Features:
# 1. D Flip-Flop Truth Table
# 2. Next-State Calculation
# 3. Clock Simulation
# 4. Set and Reset
# 5. Multiple Clock Cycles
# 6. Binary D Flip-Flop Register Simulation


def d_flip_flop_truth_table():
    """Display the truth table of a D flip-flop."""

    print("\n========== D FLIP-FLOP TRUTH TABLE ==========")

    print("\nD\tClock\tQ(next)")
    print("-------------------")

    print("0\t↑\t0")
    print("1\t↑\t1")

    print("\n↑ = Rising edge of clock")


def next_state():
    """Calculate the next state of a D flip-flop."""

    print("\n========== NEXT STATE CALCULATION ==========")

    q_current = input("Enter current Q (0/1): ")
    d = input("Enter D input (0/1): ")

    if q_current not in ["0", "1"] or d not in ["0", "1"]:
        print("Error: Enter only 0 or 1.")
        return

    q_next = d

    print("\nCurrent State Q =", q_current)
    print("D Input         =", d)
    print("Next State Q    =", q_next)

    if q_next == q_current:
        print("State remains unchanged.")
    else:
        print("State changes on the clock edge.")


def clock_simulation():
    """Simulate a D flip-flop for multiple clock cycles."""

    print("\n========== CLOCK SIMULATION ==========")

    d_sequence = input(
        "Enter D input sequence (example: 10110): "
    )

    if not all(bit in "01" for bit in d_sequence):
        print("Error: Enter only binary values.")
        return

    q = "0"

    print("\nClock\tD\tQ")

    for clock, d in enumerate(d_sequence, start=1):
        q = d
        print(f"{clock}\t{d}\t{q}")


def set_reset_operation():
    """Demonstrate asynchronous set and reset."""

    print("\n========== SET / RESET OPERATION ==========")

    print("Enter:")
    print("1. Normal Operation")
    print("2. Set")
    print("3. Reset")

    choice = input("Enter your choice: ")

    if choice == "1":
        d = input("Enter D (0/1): ")

        if d not in ["0", "1"]:
            print("Error: D must be 0 or 1.")
            return

        print(f"D = {d}")
        print(f"Q(next) = {d}")

    elif choice == "2":
        print("SET activated.")
        print("Q = 1")

    elif choice == "3":
        print("RESET activated.")
        print("Q = 0")

    else:
        print("Invalid choice.")


def register_simulation():
    """Simulate a group of D flip-flops as a register."""

    print("\n========== D FLIP-FLOP REGISTER ==========")

    data = input("Enter binary data (example: 1011): ")

    if not data or not all(bit in "01" for bit in data):
        print("Error: Enter only binary values.")
        return

    register = ["0"] * len(data)

    print("\nInitial Register:")
    print("".join(register))

    print("\nClock\tD Input\tQ Output")

    for clock, bit in enumerate(data, start=1):

        register[clock - 1] = bit

        print(
            f"{clock}\t{bit}\t{''.join(register)}"
        )

    print("\nFinal Register:")
    print("".join(register))


def excitation_table():
    """Display the excitation table of a D flip-flop."""

    print("\n========== D FLIP-FLOP EXCITATION TABLE ==========")

    print("\nQ(current)\tQ(next)\tD")
    print("--------------------------------")

    print("0\t\t0\t0")
    print("0\t\t1\t1")
    print("1\t\t0\t0")
    print("1\t\t1\t1")

    print("\nCharacteristic equation:")
    print("Q(next) = D")


def main():

    while True:

        print("\n==============================================")
        print("        D FLIP-FLOP CALCULATOR")
        print("        Digital Circuits")
        print("        Electrical Engineering")
        print("==============================================")

        print("1. D Flip-Flop Truth Table")
        print("2. Next-State Calculation")
        print("3. Clock Simulation")
        print("4. Set / Reset Operation")
        print("5. D Flip-Flop Register")
        print("6. Excitation Table")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":
                d_flip_flop_truth_table()

            elif choice == "2":
                next_state()

            elif choice == "3":
                clock_simulation()

            elif choice == "4":
                set_reset_operation()

            elif choice == "5":
                register_simulation()

            elif choice == "6":
                excitation_table()

            elif choice == "7":
                print(
                    "\nThank you for using "
                    "D Flip-Flop Calculator!"
                )
                break

            else:
                print("\nInvalid choice. Please select 1-7.")

        except ValueError:
            print("\nPlease enter a valid value.")


if __name__ == "__main__":
    main()
