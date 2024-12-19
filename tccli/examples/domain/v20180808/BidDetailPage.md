**Example 1: 预释放详情页出价**



Input: 

```
tccli domain BidDetailPage --cli-unfold-argument  \
    --BusinessId P00***61
```

Output: 
```
{
    "Response": {
        "Domain": "dte.com",
        "CurrentPrice": 120,
        "BidPrice": 100,
        "CurrentPriceScope": 50,
        "PriceScope": [
            {
                "MaxPrice": 0,
                "MinPrice": 0,
                "Price": 0,
                "DepositPrice": 0
            }
        ],
        "DepositPrice": 120,
        "RequestId": "dwert-dwer-werq-dwerg"
    }
}
```

