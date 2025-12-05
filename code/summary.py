def export_outputs(df, daily, weekly, building_summary):
    df.to_csv("output/cleaned_energy_data.csv", index=False)
    building_summary.to_csv("output/building_summary.csv")

    total_consumption = df["kwh"].sum()
    highest_building = building_summary["total"].idxmax()

    with open("output/summary.txt", "w") as f:
        f.write("=== Campus Energy Summary ===\n")
        f.write(f"Total Consumption: {total_consumption} kWh\n")
        f.write(f"Highest Consuming Building: {highest_building}\n")
        f.write(f"Peak Day Load: {daily.max()} kWh\n")
        f.write(f"Peak Week Load: {weekly.max()} kWh\n")
