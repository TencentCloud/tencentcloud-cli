**Example 1: 请求成功**

请求成功

Input: 

```
tccli domain DescribeIntlDomainPriceNewList --cli-unfold-argument  \
    --Operation renew \
    --TldList .com \
    --Year 1
```

Output: 
```
{
    "Response": {
        "PriceList": [
            {
                "Title": "com域名新注",
                "Tld": ".com",
                "Operation": "new",
                "Year": 1,
                "Price": 12.99,
                "RealPrice": 12.99
            }
        ],
        "RequestId": "dewer-dweq-pfwe-fpwer"
    }
}
```

**Example 2: 获取域名价格列表**

获取域名价格列表

Input: 

```
tccli domain DescribeIntlDomainPriceNewList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PriceList": [
            {
                "Title": "com域名新注",
                "Tld": ".com",
                "Operation": "new",
                "Year": 1,
                "Price": 12.99,
                "RealPrice": 12.99
            }
        ],
        "RequestId": "dewer-dweq-pfwe-fpwer"
    }
}
```

