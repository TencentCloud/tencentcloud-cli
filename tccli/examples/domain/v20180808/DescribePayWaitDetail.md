**Example 1: 等待支付详情接口**



Input: 

```
tccli domain DescribePayWaitDetail --cli-unfold-argument  \
    --BusinessId abc
```

Output: 
```
{
    "Response": {
        "Domain": "abc",
        "Status": "abc",
        "EndTime": "abc",
        "RegTime": "abc",
        "Price": 0,
        "RetDeposit": 0,
        "RequestId": "abc"
    }
}
```

