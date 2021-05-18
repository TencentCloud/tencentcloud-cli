**Example 1: 拉取账户流水**



Input: 

```
tccli iotvideo DescribeBalanceTransactions --cli-unfold-argument  \
    --Operation CreateOrder \
    --Limit 10 \
    --AccountType 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9d6e94e0-4552-4ab3-86fe-1f767db2ceba",
        "TotalCount": 12,
        "Transactions": [
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "a5b504ba-acab-43d1-8694-bcd5ce0f0802",
                "Amount": 90,
                "Balance": 99990010,
                "OperationTime": 1611830100
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "19f9d419-4db5-4cb5-9242-3f245dd1627c",
                "Amount": 900,
                "Balance": 99990100,
                "OperationTime": 1609147842
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "01bcd194-e330-478e-b7df-2912f52cfc80",
                "Amount": 900,
                "Balance": 99991000,
                "OperationTime": 1609147835
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "51ecad70-262b-4251-a536-345c1c0b31e9",
                "Amount": 900,
                "Balance": 99991900,
                "OperationTime": 1609147651
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "cc7c13d5-c838-4588-89be-6b354af48adf",
                "Amount": 900,
                "Balance": 99992800,
                "OperationTime": 1609147330
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "4a4db67c-9b9f-46e4-9eec-59cc0ed41ebc",
                "Amount": 900,
                "Balance": 99993700,
                "OperationTime": 1609147235
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "4f27575e-5002-492b-84ed-fca0a40b5f6c",
                "Amount": 900,
                "Balance": 99994600,
                "OperationTime": 1609146690
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "fdd0d195-a23a-4129-a22c-46a53c13a5c0",
                "Amount": 900,
                "Balance": 99995500,
                "OperationTime": 1609146311
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "849e416b-8d02-449f-ba17-4e479e5e3810",
                "Amount": 900,
                "Balance": 99996400,
                "OperationTime": 1609145974
            },
            {
                "AccountType": 1,
                "Operation": "CreateOrder",
                "DealId": "12a0ef42-ceec-4078-879b-a45d2d78b154",
                "Amount": 900,
                "Balance": 99997300,
                "OperationTime": 1609145857
            }
        ]
    }
}
```

