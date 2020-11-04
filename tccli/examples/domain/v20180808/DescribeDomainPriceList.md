**Example 1: 获取域名价格列表**



Input: 

```
tccli domain DescribeDomainPriceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PriceList": [
            {
                "Operation": "redem",
                "Price": 1000,
                "Year": 1,
                "RealPrice": 1000,
                "Tld": ".work"
            },
            {
                "Operation": "tran",
                "Price": 30,
                "Year": 1,
                "RealPrice": 30,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 270,
                "Year": 9,
                "RealPrice": 270,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 210,
                "Year": 7,
                "RealPrice": 210,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 240,
                "Year": 8,
                "RealPrice": 240,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 180,
                "Year": 6,
                "RealPrice": 180,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 120,
                "Year": 4,
                "RealPrice": 120,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 150,
                "Year": 5,
                "RealPrice": 150,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 90,
                "Year": 3,
                "RealPrice": 90,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 30,
                "Year": 1,
                "RealPrice": 30,
                "Tld": ".work"
            },
            {
                "Operation": "renew",
                "Price": 60,
                "Year": 2,
                "RealPrice": 60,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 295,
                "Year": 10,
                "RealPrice": 295,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 265,
                "Year": 9,
                "RealPrice": 265,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 235,
                "Year": 8,
                "RealPrice": 235,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 205,
                "Year": 7,
                "RealPrice": 205,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 175,
                "Year": 6,
                "RealPrice": 175,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 145,
                "Year": 5,
                "RealPrice": 155,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 115,
                "Year": 4,
                "RealPrice": 115,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 85,
                "Year": 3,
                "RealPrice": 85,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 55,
                "Year": 2,
                "RealPrice": 55,
                "Tld": ".work"
            },
            {
                "Operation": "new",
                "Price": 25,
                "Year": 1,
                "RealPrice": 25,
                "Tld": ".work"
            },
            {
                "Operation": "redem",
                "Price": 1000,
                "Year": 1,
                "RealPrice": 1000,
                "Tld": ".top"
            },
            {
                "Operation": "tran",
                "Price": 30,
                "Year": 1,
                "RealPrice": 30,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 270,
                "Year": 9,
                "RealPrice": 270,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 240,
                "Year": 8,
                "RealPrice": 240,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 210,
                "Year": 7,
                "RealPrice": 210,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 180,
                "Year": 6,
                "RealPrice": 180,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 150,
                "Year": 5,
                "RealPrice": 150,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 120,
                "Year": 4,
                "RealPrice": 120,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 90,
                "Year": 3,
                "RealPrice": 90,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 60,
                "Year": 2,
                "RealPrice": 60,
                "Tld": ".top"
            },
            {
                "Operation": "renew",
                "Price": 30,
                "Year": 1,
                "RealPrice": 30,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 295,
                "Year": 10,
                "RealPrice": 295,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 265,
                "Year": 9,
                "RealPrice": 265,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 235,
                "Year": 8,
                "RealPrice": 235,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 205,
                "Year": 7,
                "RealPrice": 205,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 175,
                "Year": 6,
                "RealPrice": 175,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 145,
                "Year": 5,
                "RealPrice": 155,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 115,
                "Year": 4,
                "RealPrice": 115,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 85,
                "Year": 3,
                "RealPrice": 85,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 55,
                "Year": 2,
                "RealPrice": 55,
                "Tld": ".top"
            },
            {
                "Operation": "new",
                "Price": 25,
                "Year": 1,
                "RealPrice": 25,
                "Tld": ".top"
            },
            {
                "Operation": "redem",
                "Price": 1000,
                "Year": 1,
                "RealPrice": 1000,
                "Tld": ".fashion"
            },
            {
                "Operation": "tran",
                "Price": 30,
                "Year": 1,
                "RealPrice": 30,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 270,
                "Year": 9,
                "RealPrice": 270,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 25,
                "Year": 1,
                "RealPrice": 25,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 55,
                "Year": 2,
                "RealPrice": 55,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 85,
                "Year": 3,
                "RealPrice": 85,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 115,
                "Year": 4,
                "RealPrice": 115,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 240,
                "Year": 8,
                "RealPrice": 240,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 180,
                "Year": 6,
                "RealPrice": 180,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 210,
                "Year": 7,
                "RealPrice": 210,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 150,
                "Year": 5,
                "RealPrice": 150,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 120,
                "Year": 4,
                "RealPrice": 120,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 90,
                "Year": 3,
                "RealPrice": 90,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 60,
                "Year": 2,
                "RealPrice": 60,
                "Tld": ".fashion"
            },
            {
                "Operation": "renew",
                "Price": 30,
                "Year": 1,
                "RealPrice": 30,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 295,
                "Year": 10,
                "RealPrice": 295,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 265,
                "Year": 9,
                "RealPrice": 265,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 235,
                "Year": 8,
                "RealPrice": 235,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 205,
                "Year": 7,
                "RealPrice": 205,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 175,
                "Year": 6,
                "RealPrice": 175,
                "Tld": ".fashion"
            },
            {
                "Operation": "new",
                "Price": 145,
                "Year": 5,
                "RealPrice": 155,
                "Tld": ".fashion"
            }
        ]
    }
}
```

