**Example 1: 根据ID查询码**

根据ID查询码

Input: 

```
tccli trp DescribeTraceCodeById --cli-unfold-argument  \
    --Code https://anxin.m.qq.com/qr/eqdmnz7020bmtvi9_000243813742005003
```

Output: 
```
{
    "Response": {
        "TraceCode": {
            "Code": "abc",
            "CorpId": 1,
            "PackId": "abc",
            "BatchId": "abc",
            "MerchantId": "abc",
            "ProductId": "abc",
            "Status": 1,
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "MerchantName": "abc",
            "ProductName": "abc",
            "AgentId": 1,
            "Level": 1
        },
        "CodePath": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

