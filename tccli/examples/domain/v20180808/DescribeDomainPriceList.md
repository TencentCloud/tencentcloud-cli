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
                "Tld": "abc",
                "Year": 1,
                "Price": 1,
                "RealPrice": 1,
                "Operation": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

