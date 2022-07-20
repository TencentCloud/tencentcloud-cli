**Example 1: 查看运营活动资源包列表**



Input: 

```
tccli iotvideo DescribeBonuses --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "48e1944a-5b92-4cfa-a215-b26883f0c116",
        "TotalCount": 1,
        "Bonuses": [
            {
                "BonusId": 3,
                "UserId": "2300001383",
                "PackageId": "device-bonus-1y10w",
                "Total": 100000,
                "Used": 0,
                "ExpireTime": 1635705286,
                "CreateTime": 1634699594
            }
        ]
    }
}
```

