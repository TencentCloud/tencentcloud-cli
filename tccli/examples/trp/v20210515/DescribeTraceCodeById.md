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
            "Status": 1,
            "UpdateTime": "xx",
            "Code": "xx",
            "MerchantName": "xx",
            "CorpId": 1,
            "PackId": "xx",
            "ProductName": "xx",
            "BatchId": "xx",
            "CreateTime": "xx",
            "MerchantId": "xx",
            "ProductId": "xx"
        },
        "RequestId": "xx"
    }
}
```

