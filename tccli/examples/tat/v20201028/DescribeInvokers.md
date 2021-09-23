**Example 1: 查询执行器**



Input: 

```
tccli tat DescribeInvokers --cli-unfold-argument  \
    --Filters.0.Name invoker-id \
    --Filters.0.Values ivk-b7s3qa5l
```

Output: 
```
{
    "Response": {
        "RequestId": "a4c828cf-31c9-42d2-a558-2ad340a76ef0",
        "TotalCount": 1,
        "InvokerSet": [
            {
                "InvokerId": "ivk-b7s3qa5l",
                "Name": "test-invoker",
                "Type": "SCHEDULE",
                "CommandId": "cmd-m7uma92n",
                "Username": "root",
                "Parameters": "{\"var\": \"1\"}",
                "InstanceIds": [
                    "ins-yx05ky8j"
                ],
                "Enable": false,
                "ScheduleSettings": {
                    "Policy": "ONCE",
                    "Recurrence": "",
                    "InvokeTime": ""
                },
                "CreatedTime": "2021-08-30T06:42:02Z",
                "UpdatedTime": "2021-09-09T12:07:00Z"
            }
        ]
    }
}
```

