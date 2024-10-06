#Input Phase
def calculate_tuition(district_code, credits):
    if district_code == 'I':
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00
    return credits * cost_per_credit


def main():
    total_tuition = 0.0
    student_count = 0

    # Process Phase
    with open("students.txt", "r") as file:

        for line in file:
            last_name, district_code, credits_str = line.strip().split(',')
            credits = int(credits_str)

            tuition = calculate_tuition(district_code, credits)
            total_tuition += tuition
            student_count += 1

            # Output Phase
            print(
                f"Student: {last_name}, Credits Taken: {credits}, Tuition Owed: ${tuition:,.2f}"
            )

    print(f"\nTotal Tuition Owed: ${total_tuition:,.2f}")
    print(f"Number of Students: {student_count}")


if __name__ == "__main__":
    main()
