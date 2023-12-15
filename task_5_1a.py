computers = {
    "pc1": {
        "os": "windows 10",
        "processor": "ADM Phenon II",
        "ram": "8 Gb",
        "sotherboard": "MSI87343",
        "HDD": "1Tb",
    },
    "pc2": {
        "os": "windows 7",
        "processor": "intel core i5 6400",
        "ram": "16 Gb",
        "sotherboard": "MSI87343",
        "HDD": "2Tb",
    },
    "pc3": {
        "os": "windows 11",
        "processor": "intel core i7 9400",
        "ram": "32 Gb",
        "sotherboard": "MSI87343",
        "HDD": "512 Gb",
    }
}

pc = input("Введите имя ПК: ")
parameter = input("Введите имя параметра: ")

print(computers[pc][parameter])