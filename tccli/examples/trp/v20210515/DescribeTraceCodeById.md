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
            "Code": "https://anxin.qq.com/q99j9ovp5c6sok7l5g",
            "CorpId": 10000,
            "PackId": "pn30msjjxwd2",
            "BatchId": "20241022112952826",
            "MerchantId": "pn30msjjxwga",
            "ProductId": "97zu51y30awe",
            "Status": 1,
            "CreateTime": "2024-10-30T07:16:21.265Z",
            "UpdateTime": "2024-10-30T07:16:21.265Z",
            "MerchantName": "商家A",
            "ProductName": "产品A",
            "AgentId": 1,
            "Level": 1
        },
        "CodePath": [
            "https://anxin.qq.com/q99j9ovp3336sok7l5"
        ],
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

