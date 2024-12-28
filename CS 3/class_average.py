def calculate_weighted_grade_average():
    # Get the number of categories
    num_categories = int(input("Enter the number of grade categories: "))
    
    # Initialize total weighted score
    total_weighted_score = 0
    total_weight = 0
    
    # Loop through each category
    for i in range(num_categories):
        category_name = input(f"\nEnter the name of category {i + 1} (e.g., Homework, Exams): ")
        weight = float(input(f"Enter the weight for {category_name} (as a percentage): ")) / 100

        # Get the total points earned and total possible points in this category
        earned_points = float(input(f"Enter the total points earned in {category_name}: "))
        possible_points = float(input(f"Enter the total possible points in {category_name}: "))
        
        # Calculate the average for this category
        category_average = (earned_points / possible_points) * 100

        # Add to the total weighted score
        total_weighted_score += category_average * weight
        total_weight += weight
    
    # Check that total weight is 100% (or 1.0) and display the result
    if total_weight == 1:
        print(f"\nYour overall grade average is: {total_weighted_score:.2f}%")
    else:
        print("\nThe total weight does not equal 100%. Please check your inputs.")

# Run the weighted grade average calculator
calculate_weighted_grade_average()

