# Mary's Shipping Program

**Mary's Shipping** is a program developed to calculate the cost of shipping packages using three shipping methods: Ground Shipping, Ground Shipping Premium, and Drone Shipping. The program determines the cheapest shipping option based on the given package weight.

## Features:
- **Ground Shipping**: Shipping method with a flat charge and a per-pound rate.
- **Ground Shipping Premium**: Faster shipping method with a fixed cost regardless of the weight.
- **Drone Shipping**: Shipping method with higher per-pound rates but no flat fee.

## How It Works:
1. **Input**: The user enters the weight of the package (in pounds).
2. **Shipping Calculations**:
    - **Ground Shipping**: Has a flat fee and a variable cost based on the weight.
    - **Ground Shipping Premium**: A fixed price of $125.00 regardless of the weight.
    - **Drone Shipping**: Higher per-pound costs but no flat fee.
3. **Output**: The program calculates the cost for each shipping method and then displays the cheapest option.

## Example Usage:

1. **Input**: Enter the weight of the package when prompted.
2. **Output**: The program will display the cost for Ground Shipping, Ground Shipping Premium, and Drone Shipping, and indicate the cheapest shipping option.

### Example:
**Input**: Enter the weight of the package (in pounds): 5.8
**Output**: Ground Shipping: $37.40; Ground Shipping Premium: $125.00; Drone Shipping: $52.20; Cheapest Shipping Option: Ground Shipping at $37.40.

## Installation Instructions:

1. Clone this repository:
  
    - git clone https://github.com/rraffaa/marys-shipping.git
    
2. Navigate to the project directory:
    
    - cd marys-shipping
    
3. Run the program:
   
    - python calculate_shipping.py
   
## Contributing:

I welcome contributions to improve this project! If you'd like to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Submit a pull request with a description of your changes.

## License:

This project is licensed under the **Apache 2.0 License**. See the LICENSE file for more details.