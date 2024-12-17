import tkinter as tk
from tkinter import messagebox

# Shipping calculation functions
def ground_shipping(weight):
    if weight <= 2:
        return (weight * 1.50) + 20.00
    elif weight <= 6:
        return (weight * 3.00) + 20.00
    elif weight <= 10:
        return (weight * 4.00) + 20.00
    else:
        return (weight * 4.75) + 20.00

def ground_shipping_premium():
    return 125.00

def drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25

def cheapest_shipping(ground_cost, premium_cost, drone_cost):
    # Determines the cheapest shipping option
    if ground_cost < premium_cost and ground_cost < drone_cost:
        return "Ground Shipping", ground_cost
    elif premium_cost < ground_cost and premium_cost < drone_cost:
        return "Ground Shipping Premium", premium_cost
    else:
        return "Drone Shipping", drone_cost

# Function to calculate and display results in the Graphical User Interface (GUI)
def calculate_shipping():
    try:
        weight = float(entry_weight.get())  # Get weight from input field
        # Calculate costs for each shipping method
        ground_cost = ground_shipping(weight)
        premium_cost = ground_shipping_premium()
        drone_cost = drone_shipping(weight)

        # Update labels with the calculated results
        result_ground.config(text=f"Ground Shipping: ${ground_cost:.2f}")
        result_premium.config(text=f"Ground Shipping Premium: ${premium_cost:.2f}")
        result_drone.config(text=f"Drone Shipping: ${drone_cost:.2f}")

        # Determine the cheapest shipping method
        shipping_method, cost = cheapest_shipping(ground_cost, premium_cost, drone_cost)
        result_cheapest.config(text=f"Cheapest Shipping Option: {shipping_method} at ${cost:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value for the weight.")

# Setting up the main window
root = tk.Tk()
root.title("Mary's Shipping Program")

# Adding components to the GUI
label = tk.Label(root, text="Enter the weight of the package (in pounds):")
label.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

btn_calculate = tk.Button(root, text="Calculate Shipping", command=calculate_shipping)
btn_calculate.pack()

# Labels to display results
result_ground = tk.Label(root, text="Ground Shipping: $0.00")
result_ground.pack()

result_premium = tk.Label(root, text="Ground Shipping Premium: $0.00")
result_premium.pack()

result_drone = tk.Label(root, text="Drone Shipping: $0.00")
result_drone.pack()

result_cheapest = tk.Label(root, text="Cheapest Shipping Option: N/A")
result_cheapest.pack()

# Starting the GUI
root.mainloop()
