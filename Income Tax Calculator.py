import tkinter as tk


def calculate_tax():
    try:
        # How much you earn each month and potion to calculate monthly tax
        monthly_salary = float(entry_salary.get())
        tax_period = period_var.get()
        annual_salary = float(entry_salary.get())
        tax_period = period_var.get()

        if tax_period.lower() == "monthly":
            annual_salary = monthly_salary * 12
        elif tax_period.lower() == "yearly":
            annual_salary = annual_salary * 12

        else:
            annual_salary = monthly_salary

            # Calculating tax based on tax bracket and how much user earns
        if annual_salary <= 237100:
            tax = annual_salary * 0.18
        elif annual_salary <= 370500:
            tax = 42678 + (annual_salary - 237100) * 0.26
        elif annual_salary <= 512800:
            tax = 77362 + (annual_salary - 370500) * 0.31
        elif annual_salary <= 673000:
            tax = 121475 + (annual_salary - 512800) * 0.36
        elif annual_salary <= 857900:
            tax = 179147 + (annual_salary - 673000) * 0.39
        elif annual_salary <= 1817000:
            tax = 251258 + (annual_salary - 857900) * 0.41
        else:
            tax = 644489 + (annual_salary - 1817000) * 0.45

        # If monthly is chosen divide by 12
        if tax_period.lower() == "monthly":
            tax /= 12

            # Displays how much tax required to pay
        result_label.config(text="Income Tax: {:.2f}".format(tax))

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

        # Income tax calculation logic based on tax bands
        # define the tax bands and rates according to your country's tax laws

        # Sample tax bands and rates (not based on the provided scenario)
        if annual_salary <= 50000:
            tax = 0
        elif annual_salary <= 100000:
            tax = (annual_salary - 50000) * 0.1
        else:
            tax = (50000 * 0.1) + ((annual_salary - 100000) * 0.2)

        if tax_period.lower() == "monthly":
            tax /= 12

        result_label.config(text="Income Tax: {:.2f}".format(tax))
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")


# Graphical user interface
root = tk.Tk()
root.title("Income Tax Calculator")

# Labels for GUI
label_salary = tk.Label(root, text="Please enter your monthly salary:")
label_salary.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

label_period = tk.Label(root, text="Monthly/Yearly:")
label_period.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

# Entry fields for GUI
entry_salary = tk.Entry(root)
entry_salary.grid(row=0, column=1, padx=10, pady=5)

period_var = tk.StringVar()
period_var.set("")  # Default value

# Entry field for tax period
entry_period = tk.Entry(root, textvariable=period_var)
entry_period.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Button that is used to calculate tax
calculate_button = tk.Button(root, text="Calculate Tax", command=calculate_tax)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label that will display result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
