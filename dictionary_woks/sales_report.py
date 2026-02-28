


sales_report={
    "sun":23000,
    "mon":16000,
    "tue":18000,
    "wed":15000,
    "thu":19000,
    "fri":19000,
    "sat":20000,
}

# display day-wise sales

total_sales = 0

for key in sales_report:

    value = sales_report[key]

    print(key,value)

    total_sales+=value

print(total_sales)

avg_sale = total_sales/len(sales_report)

print(avg_sale)


for key in sales_report:

    value = sales_report[key]

    if value < avg_sale:

        print("day with low sale",key,value)

# total_sale

# display avg_sales

# dispaly day  where  sales < avg_sales