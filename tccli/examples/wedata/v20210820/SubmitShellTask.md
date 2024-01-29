**Example 1: 请求demo**

请求demo

Input: 

```
tccli wedata SubmitShellTask --cli-unfold-argument  \
    --ScriptContent echo 'hello' \
    --ProjectId 345 \
    --GroupId 456 \
    --ScriptPath /tmp \
    --ScriptName BASH \
    --ScriptType SHELL \
    --RunParams {"name":"Tom", "age":123}
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Record": {
            "Id": 1,
            "ScriptContent": "echo 1",
            "CreateTime": "2021-09-22T00:00:00+00:00",
            "Status": "RUNNING",
            "InstanceId": "20220218143949840_2022-03-02T17:19:38+08:00"
        },
        "Details": [
            {
                "Id": 1,
                "ScriptContent": "echo 1",
                "StartTime": "2021-09-22T00:00:00+00:00",
                "EndTime": "2020-09-22T00:00:00+00:00",
                "Status": "RUNNING",
                "RecordId": 1
            }
        ]
    }
}
```

**Example 2: 提交SHELL任务**

提交SHELL任务

Input: 

```
tccli wedata SubmitShellTask --cli-unfold-argument  \
    --ScriptType SHELL \
    --ProjectId 1 \
    --ScriptContent echo 1 \
    --ScriptName BASH \
    --ScriptPath  \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9ae7946a-1530-4f7f-9b9c-fb9b1fec2036",
        "Record": {
            "Id": 892,
            "InstanceId": "20220218143949840_2022-03-02T19:13:37+08:00",
            "ScriptContent": "echo 1",
            "CreateTime": "2022-03-02T19:13:37+08:00",
            "Status": null
        },
        "Details": [
            {
                "Id": 892,
                "ScriptContent": "echo 1",
                "StartTime": null,
                "EndTime": null,
                "Status": "CREATED",
                "RecordId": 892
            }
        ]
    }
}
```

