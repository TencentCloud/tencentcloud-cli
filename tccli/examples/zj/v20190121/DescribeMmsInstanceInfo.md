**Example 1: DescribeMmsInstanceInfo**



Input: 

```
tccli zj DescribeMmsInstanceInfo --cli-unfold-argument  \
    --License xxx \
    --InstanceId 1256886
```

Output: 
```
{
    "Response": {
        "Data": {
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
        },
        "RequestId": "87242041-7de8-4562-96ac-2d853eca3e44"
    }
}
```

