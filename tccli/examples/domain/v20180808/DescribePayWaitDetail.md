**Example 1: 等待支付详情接口**



Input: 

```
tccli domain DescribePayWaitDetail --cli-unfold-argument  \
    --BusinessId ***561
```

Output: 
```
{
    "Response": {
        "RequestId": "45559f25-13b9-42fd-b2ae-698842d91fd7",
        "Domain": "*1.top",
        "Status": "pay",
        "EndTime": "2024-12-19 07:24:25",
        "RegTime": "2023-11-11 07:24:25",
        "Price": 98,
        "RetDeposit": 32
    }
}
```

