**Example 1: Querying rollback time range**



Input: 

```
tccli cdb DescribeRollbackRangeTime --cli-unfold-argument  \
    --InstanceIds cdb-fix44sxh cdb-bdf7h3j1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 2,
        "Items": [
            {
                "InstanceId": "cdb-fix44sxh",
                "Message": "ok",
                "Code": 0,
                "Times": [
                    {
                        "Begin": "2017-08-21 02:06:20",
                        "End": "2017-08-25 17:52:05"
                    }
                ]
            },
            {
                "InstanceId": "cdb-bdf7h3j1",
                "Message": "ok",
                "Code": 0,
                "Times": [
                    {
                        "Begin": "2017-08-21 02:06:00",
                        "End": "2017-08-25 17:52:05"
                    }
                ]
            }
        ]
    }
}
```

