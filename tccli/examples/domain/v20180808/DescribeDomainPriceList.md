**Example 1: 获取域名价格列表**

获取域名价格列表

Input: 

```
tccli domain DescribeDomainPriceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PriceList": [
            {
                "Operation": "renew",
                "Price": 266,
                "Year": 7,
                "RealPrice": 266,
                "Tld": ".pw"
            }
        ],
        "RequestId": "derft-dwer-csge-eqwrt"
    }
}
```

