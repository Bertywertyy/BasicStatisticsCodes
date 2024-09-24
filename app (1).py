import streamlit as st
import statistics

# Title of the application
st.title("Statistics Calculator")

# Input: Get user input as a string and split it into a list
input_numbers = st.text_input("Enter numbers separated by commas:")

if input_numbers:
    # Convert input strings to a list of floats
    try:
        numbers = [float(num) for num in input_numbers.split(',') if num]
        
        if len(numbers) > 0:
            # Calculate statistics
            stats = {
                'Mean': statistics.mean(numbers),
                'Median': statistics.median(numbers),
                'Mode': statistics.mode(numbers) if len(set(numbers)) != len(numbers) else '無',
                'Standard Deviation': statistics.stdev(numbers),
                'Variance': statistics.variance(numbers),
                'Population Standard Deviation': statistics.pstdev(numbers),
                'Population Variance': statistics.pvariance(numbers),
                'Max': max(numbers),
                'Min': min(numbers)
            }
            
            # Display results
            st.subheader("Statistics Results:")
            for stat, value in stats.items():
                st.write(f"{stat}: {value}")
        else:
            st.warning("Please enter at least one number.")
    
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")

