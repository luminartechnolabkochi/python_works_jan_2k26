


fr = open("fileoperations\\flight.txt")


flight = []

for line in fr:

    data = line.rstrip("\n").split(",")#["1949","January","112"]

    pssenger_data = {"year":data[0],"month":data[1],"passengers":int(data[2])}

    flight.append(pssenger_data)

year_wise_count = {}#{1950:252,1951:270}

for p in flight:
    # p={year:1951,month:feb,passenger:170}

    year = p.get("year")#1951

    p_count = p.get("passengers")#170

    if year in year_wise_count:

        year_wise_count[year]+=p_count

    else:

        year_wise_count[year]=p_count

print(year_wise_count)#{1951:123,1952:345}

year_wise_count_sorted = sorted(year_wise_count,key=year_wise_count.get)

print(year_wise_count_sorted)




