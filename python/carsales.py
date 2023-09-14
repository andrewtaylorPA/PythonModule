companies = []
sales = []

### open cars.csv
carsalesvar = open("python/car.csv")

for line in carsalesvar:
    data = line.split(",")
    
    company = data[0]
    companies.append(company)

    salesnumbers = [int(x) for x in data[1:]]
    sales.append(salesnumbers)

print(companies)
print(sales)

### sum of cars sold each month
month = (int(0))
for x in range(0,8):
    print(month)
    monthlysalesford = sales[0][month]
    monthlysalesvw = sales[1][month]
    monthlysalesmerc = sales[2][month]
    monthlysalesvh = sales[3][month]
    monthlysalesbmw = sales[4][month]
    totalmonthly = monthlysalesford + monthlysalesvw + monthlysalesmerc + monthlysalesvh + monthlysalesbmw
    print("Total monthly sales - Month:", month,":", totalmonthly)
    month = month + 1

### Yearly sales per manufacturer 
fordsales = sum(sales[0])
vwsales = sum(sales[1])
mercsales = sum(sales[2])
vhsales = sum(sales[3])
bmwsales = sum(sales[4])
print("Total yearly ford sales: ", fordsales)
print("Total yearly VW sales: ", vwsales)
print("Total yearly Merc sales: ", mercsales)
print("Total yearly Vauxhall sales: ", vhsales)
print("Total yearly BMW sales: ", bmwsales)