# Problem: currencyDivider
amount = int(input("Enter an amount: "))

n2000 = amount // 2000
amount %= 2000

n500 = amount // 500
amount %= 500

n100 = amount // 100
amount %= 100

if amount == 0:
    print(f"You can evenly divide notes into 2000-{n2000}, 500-{n500}, 100-{n100} notes")
else:
    print(
        f"You cannot evenly divide notes. "
        f"You need 2000-{n2000}, 500-{n500}, 100-{n100} notes "
        f"and additionally {amount} rupees"
    )
