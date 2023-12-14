**Example 1: 获取域名价格列表**

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
                "Tld": "abc",
                "Year": 1,
                "Price": 0,
                "RealPrice": 0,
                "Operation": "abc",
                "Title": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 请求成功**

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
                "Tld": "abc",
                "Year": 1,
                "Price": 0,
                "RealPrice": 0,
                "Operation": "abc",
                "Title": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

