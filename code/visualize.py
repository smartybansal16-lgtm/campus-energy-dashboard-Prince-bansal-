import matplotlib.pyplot as plt

def generate_dashboard(daily, weekly, building_summary, output="output/dashboard.png"):
    fig, axs = plt.subplots(3, 1, figsize=(12, 16))

    # Trend line
    axs[0].plot(daily.index, daily.values)
    axs[0].set_title("Daily Energy Consumption")
    axs[0].set_xlabel("Date")
    axs[0].set_ylabel("kWh")

    #  Bar chart
    axs[1].bar(building_summary.index, building_summary["mean"])
    axs[1].set_title("Average Weekly Usage per Building")
    axs[1].set_ylabel("Mean kWh")

    #  Scatter plot
    axs[2].scatter(weekly.index, weekly.values)
    axs[2].set_title("Weekly Peak-Hour Consumption")
    axs[2].set_xlabel("Week")
    axs[2].set_ylabel("kWh")

    plt.tight_layout()
    plt.savefig(output)
