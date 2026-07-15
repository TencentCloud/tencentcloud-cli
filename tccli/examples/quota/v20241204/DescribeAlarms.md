**Example 1: 规则列表**



Input: 

```
tccli quota DescribeAlarms --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --ProductId 1
```

Output: 
```
{
    "Response": {
        "Count": 5,
        "Data": [
            {
                "Id": 102,
                "OwnerUin": 100026600000,
                "MemberUin": 100026600000,
                "Name": "234",
                "ProductId": 13,
                "Status": 2,
                "QuotaId": 2828,
                "ProductName": "腾讯云助手",
                "QuotaName": "配额名称001",
                "Metrics": 1,
                "Threshold": 2,
                "Frequency": 1
            }
        ],
        "RequestId": "e3836e25-700a-4759-bba2-7bcd57b9ab86"
    }
}
```

