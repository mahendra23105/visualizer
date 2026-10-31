import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class SalesDataAnalyzer:

    def __init__(self):
        self.df = None

    def __del__(self):
        pass

    # Load CSV file
    def load_data(self):
        if not os.path.exists("sales_data.csv"):
            data = {
                "Date": ["2026-01-01", "2026-01-02", "2026-01-03",
                         "2026-01-04", "2026-01-05"],
                "Product": ["Laptop", "Mobile", "Tablet",
                            "Laptop", "Mobile"],
                "Region": ["Ahmedabad", "Surat", "Rajkot",
                           "Ahmedabad", "Surat"],
                "Sales": [50000, 20000, 15000, 55000, 25000],
                "Profit": [5000, 3000, 2000, 6000, 4000]
            }

            pd.DataFrame(data).to_csv("sales_data.csv", index=False)

        try:
            self.df = pd.read_csv("sales_data.csv")
            print("Data loaded successfully!")
            print(self.df)

        except Exception as e:
            print("Error:", e)

    # Explore data
    def explore_data(self):
        if self.df is not None:
            print("\nFirst 5 Records:")
            print(self.df.head())

            print("\nDataset Information:")
            print(self.df.info())

            print("\nStatistics:")
            print(self.df.describe())

        else:
            print("Please load data first!")

    # Clean data
    def clean_data(self):
        if self.df is not None:
            self.df = self.df.drop_duplicates()
            self.df = self.df.dropna()

            print("Data cleaned successfully!")
            print(self.df)

        else:
            print("Load data first!")

    # Convert DataFrame to NumPy
    def numpy_array(self):
        if self.df is not None:
            arr = self.df["Sales"].to_numpy()

            print("NumPy Array:", arr)
            print("First Value:", arr[0])
            print("Sliced Array:", arr[0:3])

        else:
            print("Load data first!")

    # Mathematical operations
    def mathematics(self):
        if self.df is not None:
            sales = self.df["Sales"]

            print("Addition:", sales + 100)
            print("Subtraction:", sales - 100)
            print("Multiplication:", sales * 2)
            print("Division:", sales / 2)

        else:
            print("Load data first!")

    # Combine and split data
    def combine_split(self):
        if self.df is None:
            print("Load data first!")
            return

        print("\n1. Combine Data")
        print("2. Split Data")

        choice = input("Enter choice: ")

        if choice == "1":
            new_data = pd.DataFrame({
                "Date": ["2026-01-06"],
                "Product": ["Tablet"],
                "Region": ["Rajkot"],
                "Sales": [18000],
                "Profit": [2500]
            })

            self.df = pd.concat(
                [self.df, new_data], ignore_index=True
            )

            print("Data combined successfully!")
            print(self.df)

        elif choice == "2":
            print("\nAhmedabad Data:")
            print(self.df[self.df["Region"] == "Ahmedabad"])

            print("\nOther Region Data:")
            print(self.df[self.df["Region"] != "Ahmedabad"])

        else:
            print("Invalid choice!")

    # Search, sort and filter
    def search_sort_filter(self):
        if self.df is None:
            print("Load data first!")
            return

        print("\n1. Search Product")
        print("2. Sort Sales")
        print("3. Filter Sales")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            print(self.df[self.df["Product"] == name])

        elif choice == "2":
            print(self.df.sort_values(
                by="Sales", ascending=False
            ))

        elif choice == "3":
            amount = int(input("Enter minimum sales: "))
            print(self.df[self.df["Sales"] > amount])

        else:
            print("Invalid choice!")

    # Aggregate functions
    def aggregate_functions(self):
        if self.df is not None:
            print("Total Sales:", self.df["Sales"].sum())
            print("Average Sales:", self.df["Sales"].mean())
            print("Maximum Sales:", self.df["Sales"].max())
            print("Minimum Sales:", self.df["Sales"].min())
            print("Total Records:", self.df["Sales"].count())

        else:
            print("Load data first!")

    # Statistical analysis
    def statistical_analysis(self):
        if self.df is not None:
            sales = self.df["Sales"]

            print("Standard Deviation:", sales.std())
            print("Variance:", sales.var())
            print("25% Percentile:", sales.quantile(0.25))
            print("50% Percentile:", sales.quantile(0.50))
            print("75% Percentile:", sales.quantile(0.75))

        else:
            print("Load data first!")

    # Pivot Table
    def pivot_table(self):
        if self.df is not None:
            result = pd.pivot_table(
                self.df,
                values="Sales",
                index="Region",
                aggfunc="sum"
            )

            print(result)

        else:
            print("Load data first!")

    # Data Visualization
    def visualize_data(self):
        if self.df is None:
            print("Load data first!")
            return

        print("\n1. Bar Chart")
        print("2. Line Chart")
        print("3. Pie Chart")
        print("4. Histogram")
        print("5. Scatter Plot")
        print("6. Heatmap")
        print("7. Box Plot")
        print("8. Stack Plot")

        choice = input("Enter choice: ")

        plt.figure(figsize=(7, 5))

        if choice == "1":
            plt.bar(self.df["Product"], self.df["Sales"])
            plt.title("Product Sales")

        elif choice == "2":
            plt.plot(self.df["Date"], self.df["Sales"], marker="o")
            plt.title("Sales Trend")
            plt.xticks(rotation=45)

        elif choice == "3":
            plt.pie(
                self.df["Sales"],
                labels=self.df["Product"],
                autopct="%1.1f%%"
            )
            plt.title("Sales Distribution")

        elif choice == "4":
            plt.hist(self.df["Sales"], bins=5)
            plt.title("Sales Histogram")

        elif choice == "5":
            plt.scatter(self.df["Sales"], self.df["Profit"])
            plt.xlabel("Sales")
            plt.ylabel("Profit")
            plt.title("Sales and Profit")

        elif choice == "6":
            sns.heatmap(
                self.df[["Sales", "Profit"]].corr(),
                annot=True
            )
            plt.title("Sales Correlation")

        elif choice == "7":
            sns.boxplot(x=self.df["Sales"])
            plt.title("Sales Box Plot")

        elif choice == "8":
            plt.stackplot(
                range(len(self.df)),
                self.df["Sales"],
                self.df["Profit"],
                labels=["Sales", "Profit"]
            )
            plt.legend()
            plt.title("Sales and Profit Stack Plot")

        else:
            print("Invalid choice!")
            plt.close()
            return

        plt.tight_layout()
        plt.savefig("sales_chart.png")
        plt.show()

        print("Chart saved as sales_chart.png")

    # Main Menu
    def menu(self):

        while True:
            print("\n===== PANDAS ANALYZER =====")
            print("1. Load Data")
            print("2. Explore Data")
            print("3. Clean Data")
            print("4. NumPy Array")
            print("5. Mathematical Operations")
            print("6. Combine and Split")
            print("7. Search, Sort and Filter")
            print("8. Aggregate Functions")
            print("9. Statistical Analysis")
            print("10. Pivot Table")
            print("11. Data Visualization")
            print("12. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.load_data()

            elif choice == "2":
                self.explore_data()

            elif choice == "3":
                self.clean_data()

            elif choice == "4":
                self.numpy_array()

            elif choice == "5":
                self.mathematics()

            elif choice == "6":
                self.combine_split()

            elif choice == "7":
                self.search_sort_filter()

            elif choice == "8":
                self.aggregate_functions()

            elif choice == "9":
                self.statistical_analysis()

            elif choice == "10":
                self.pivot_table()

            elif choice == "11":
                self.visualize_data()

            elif choice == "12":
                print("Thank you for using Pandas Analyzer!")
                break

            else:
                print("Invalid choice! Try again.")


if __name__ == "__main__":
    obj = SalesDataAnalyzer()
    obj.menu()
