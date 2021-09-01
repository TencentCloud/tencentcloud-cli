**Example 1: DescribeMmsInstanceList**



Input: 

```
tccli zj DescribeMmsInstanceList --cli-unfold-argument  \
    --License xxx \
    --AppSubId 1256886009 \
    --Title  11 \
    --Offset 0 \
    --Limit 907
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 2,
            "List": [
                {
                    "InstanceId": 123456,
                    "InstanceName": "test",
                    "Status": 1,
                    "StatusInfo": [
                        {
                            "Operator": "gmcc",
                            "State": 1
                        },
                        {
                            "Operator": "unicom",
                            "State": 1
                        },
                        {
                            "Operator": "cdma",
                            "State": 0
                        }
                    ],
                    "AppSubId": "MBOSS1542",
                    "Title": "test",
                    "Sign": "",
                    "Contents": "test data",
                    "CreatedAt": "0001-01-01 00:00:00"
                }
            ]
        },
        "RequestId": "b3b2d6fd-5484-4d4f-a2a2-9eb76e818325"
    }
}
```

