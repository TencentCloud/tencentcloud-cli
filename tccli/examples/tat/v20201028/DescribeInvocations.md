**Example 1: 查询执行活动**



Input: 

```
tccli tat DescribeInvocations --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --InvocationIds inv-q4zp60g0
```

Output: 
```
{
    "Response": {
        "RequestId": "958a3603-d0c3-4c97-a37d-6bc24eacddac",
        "TotalCount": 1,
        "InvocationSet": [
            {
                "CommandId": "cmd-9dxzty3m",
                "CommandContent": "cHdk",
                "CommandType": "SHELL",
                "Timeout": 60,
                "InvocationSource": "USER",
                "WorkingDirectory": "/root",
                "InvocationId": "inv-q4zp60g0",
                "InstanceKind": "CVM",
                "InvocationStatus": "SUCCESS",
                "Description": "Test Invocation",
                "Parameters": "",
                "DefaultParameters": "",
                "Username": "root",
                "OutputCOSKeyPrefix": "cosprefix",
                "OutputCOSBucketUrl": "https://example-123456789.cos.ap-beijing.myqcloud.com",
                "InvocationTaskBasicInfoSet": [
                    {
                        "InvocationTaskId": "invt-kakne8h2",
                        "TaskStatus": "SUCCESS",
                        "InstanceId": "ins-zj0f57ew"
                    },
                    {
                        "InvocationTaskId": "invt-jc2onrxm",
                        "TaskStatus": "SUCCESS",
                        "InstanceId": "ins-zj0f57ex"
                    },
                    {
                        "InvocationTaskId": "invt-6xmuisyq",
                        "TaskStatus": "SUCCESS",
                        "InstanceId": "ins-zj0f57ev"
                    }
                ],
                "StartTime": "2020-11-09T07:21:59+00:00",
                "EndTime": "2020-11-09T07:22:08+00:00",
                "CreatedTime": "2020-11-09T07:21:59+00:00",
                "UpdatedTime": "2020-11-09T07:22:08+00:00"
            }
        ]
    }
}
```

