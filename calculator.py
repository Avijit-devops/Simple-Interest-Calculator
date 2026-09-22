def calculate_simple_interest(principal: float, rate: float, time: float):
    interest = (principal * rate * time) / 100
    total = principal + interest
    return interest, total

if __name__ == "__main__":
    p = float(input("Enter Principal amount: "))
    r = float(input("Enter Annual Interest Rate (%): "))
    t = float(input("Enter Time (in years): "))

    interest, total = calculate_simple_interest(p, r, t)
    print(f"\nSimple Interest: {interest:.2f}")
    print(f"Total Amount: {total:.2f}")