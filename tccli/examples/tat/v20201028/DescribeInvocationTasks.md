**Example 1: 根据执行活动ID查询所有执行任务详情**



Input: 

```
tccli tat DescribeInvocationTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --HideOutput False \
    --Filters.0.Name invocation-id \
    --Filters.0.Values inv-1vll7hda
```

Output: 
```
{
    "Response": {
        "RequestId": "a1df9725-51c6-466d-a038-4c86461a8e26",
        "TotalCount": 3,
        "InvocationTaskSet": [
            {
                "CommandId": "cmd-13axrtuq",
                "CommandDocument": {
                    "Content": "d2hvYW1p",
                    "CommandType": "SHELL",
                    "Timeout": 1,
                    "Username": "root",
                    "WorkingDirectory": "/root/"
                },
                "InvocationId": "inv-1vll7hda",
                "InvocationTaskId": "invt-afwuqts2",
                "TaskStatus": "SUCCESS",
                "InstanceId": "ins-zj0f57ev",
                "TaskResult": {
                    "ExitCode": 0,
                    "Output": "cm9vdAo=",
                    "Dropped": 0,
                    "OutputUploadCOSErrorInfo": "",
                    "OutputUrl": "",
                    "ExecStartTime": "2020-11-05T07:49:58+00:00",
                    "ExecEndTime": "2020-11-05T07:50:04+00:00"
                },
                "ErrorInfo": "",
                "InvocationSource": "xx",
                "StartTime": "2020-11-05T07:49:58+00:00",
                "EndTime": "2020-11-05T07:50:04+00:00",
                "CreatedTime": "2020-11-05T07:49:56+00:00",
                "UpdatedTime": "2020-11-05T07:50:06+00:00"
            },
            {
                "CommandId": "cmd-13axrtuq",
                "CommandDocument": {
                    "Content": "d2hvYW1p",
                    "CommandType": "SHELL",
                    "Timeout": 1,
                    "Username": "root",
                    "WorkingDirectory": "/root/"
                },
                "InvocationId": "inv-1vll7hda",
                "InvocationTaskId": "invt-08oe5fe2",
                "TaskStatus": "SUCCESS",
                "InstanceId": "ins-zj0f57ex",
                "TaskResult": {
                    "ExitCode": 0,
                    "Output": "cm9vdAo=",
                    "Dropped": 0,
                    "OutputUploadCOSErrorInfo": "",
                    "OutputUrl": "",
                    "ExecStartTime": "2020-11-05T07:49:58+00:00",
                    "ExecEndTime": "2020-11-05T07:50:04+00:00"
                },
                "ErrorInfo": "",
                "InvocationSource": "xx",
                "StartTime": "2020-11-05T07:49:58+00:00",
                "EndTime": "2020-11-05T07:50:04+00:00",
                "CreatedTime": "2020-11-05T07:49:56+00:00",
                "UpdatedTime": "2020-11-05T07:50:06+00:00"
            },
            {
                "CommandId": "cmd-13axrtuq",
                "CommandDocument": {
                    "Content": "d2hvYW1p",
                    "CommandType": "SHELL",
                    "Timeout": 1,
                    "Username": "root",
                    "WorkingDirectory": "/root/"
                },
                "InvocationId": "inv-1vll7hda",
                "InvocationTaskId": "invt-91cpqs22",
                "TaskStatus": "SUCCESS",
                "InstanceId": "ins-zj0f57ew",
                "TaskResult": {
                    "ExitCode": 0,
                    "Output": "cm9vdAo=",
                    "Dropped": 0,
                    "OutputUploadCOSErrorInfo": "",
                    "OutputUrl": "",
                    "ExecStartTime": "2020-11-05T07:49:58+00:00",
                    "ExecEndTime": "2020-11-05T07:50:04+00:00"
                },
                "ErrorInfo": "",
                "InvocationSource": "xx",
                "StartTime": "2020-11-05T07:49:58+00:00",
                "EndTime": "2020-11-05T07:50:04+00:00",
                "CreatedTime": "2020-11-05T07:49:56+00:00",
                "UpdatedTime": "2020-11-05T07:50:06+00:00"
            }
        ]
    }
}
```

