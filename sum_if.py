sales_july = [
    ["Store A", "Tokyo", 5000],
    ["Store B", "Osaka", 3000],
    ["Store C", "Tokyo", 7000],
    ["Store D", "Fukuoka", 4000],
    ["Store E", "Osaka", 2000]
]



def get_unique_regions(sales_data):
    return set(region for _, region, _ in sales_data)

def sum_sales_by_region(sales_data, region):
    return sum(sales for _, r, sales in sales_data if r == region)


def sum_sales_by_all_regions(sales_data):
    regions = get_unique_regions(sales_data)
    return {region: sum_sales_by_region(sales_data, region) for region in regions}

print(sum_sales_by_all_regions(sales_july))

