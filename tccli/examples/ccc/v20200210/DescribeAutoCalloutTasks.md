**Example 1: 示例**



Input: 

```
tccli ccc DescribeAutoCalloutTasks --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10 \
    --SdkAppId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Tasks": [
            {
                "TaskId": 3241,
                "IvrId": 1,
                "CalleeCount": 1,
                "Name": "foobar",
                "NotBefore": 0,
                "NotAfter": 0,
                "State": 1,
                "Callers": [
                    "123456"
                ]
            }
        ],
        "RequestId": "123456"
    }
}
```

