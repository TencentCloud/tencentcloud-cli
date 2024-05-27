**Example 1: 预释放详情页出价**



Input: 

```
tccli domain BidDetailPage --cli-unfold-argument  \
    --BusinessId abc
```

Output: 
```
{
    "Response": {
        "Domain": "abc",
        "CurrentPrice": 0,
        "BidPrice": 0,
        "CurrentPriceScope": 0,
        "PriceScope": [
            {
                "MaxPrice": 0,
                "MinPrice": 0,
                "Price": 0,
                "DepositPrice": 0
            }
        ],
        "DepositPrice": 0,
        "RequestId": "abc"
    }
}
```

