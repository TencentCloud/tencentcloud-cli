**Example 1: 获取自定义脚本任务列表**



Input: 

```
tccli bm DescribeUserCmdTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --OrderField RunBeginTime \
    --Order 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "UserCmdTasks": [
            {
                "TaskId": "cmdtask-1ghosm17",
                "Status": -1,
                "Alias": "marsinfan",
                "CmdId": "cmd-dr3ja3hq",
                "InstanceCount": 2,
                "SuccessCount": 0,
                "FailureCount": 0,
                "RunBeginTime": "2018-09-20 17:42:21",
                "RunEndTime": ""
            },
            {
                "TaskId": "cmdtask-2obesa6h",
                "Status": -1,
                "Alias": "marsinfan",
                "CmdId": "cmd-dr3ja3hq",
                "InstanceCount": 1,
                "SuccessCount": 0,
                "FailureCount": 0,
                "RunBeginTime": "2018-09-10 21:09:49",
                "RunEndTime": ""
            },
            {
                "TaskId": "cmdtask-mi5k1o5p",
                "Status": -1,
                "Alias": "marsinfan",
                "CmdId": "cmd-dr3ja3hq",
                "InstanceCount": 1,
                "SuccessCount": 0,
                "FailureCount": 0,
                "RunBeginTime": "2018-09-10 21:06:52",
                "RunEndTime": ""
            },
            {
                "TaskId": "cmdtask-jjbalbah",
                "Status": -1,
                "Alias": "1",
                "CmdId": "cmd-bugfk68c",
                "InstanceCount": 1,
                "SuccessCount": 0,
                "FailureCount": 0,
                "RunBeginTime": "2018-09-10 20:57:09",
                "RunEndTime": ""
            }
        ],
        "RequestId": "c63330d9-0e57-4c7e-a34e-3e228d58ebc6"
    }
}
```

