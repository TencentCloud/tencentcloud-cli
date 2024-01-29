**Example 1: 请求demo**

请求demo

Input: 

```
tccli wedata SubmitPythonTask --cli-unfold-argument  \
    --ScriptContent print(1) \
    --ProjectId 345 \
    --GroupId 456 \
    --ScriptPath /tmp \
    --ScriptType PYTHON \
    --ScriptName PYTHON3 \
    --RunParams {"name":"Tom", "age":123}
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Record": {
            "Id": 1,
            "ScriptContent": "select 1",
            "CreateTime": "2021-09-22T00:00:00+00:00",
            "Status": "RUNNING",
            "InstanceId": "20220223194219292_2022-03-02T23:13:24+08:00"
        },
        "Details": [
            {
                "Id": 1,
                "ScriptContent": "select 1",
                "StartTime": "2021-09-22T00:00:00+00:00",
                "EndTime": "2020-09-22T00:00:00+00:00",
                "Status": "RUNNING",
                "RecordId": 1
            }
        ]
    }
}
```

**Example 2: 即席分析提交python任务**

即席分析提交python任务

Input: 

```
tccli wedata SubmitPythonTask --cli-unfold-argument  \
    --ScriptType PYTHON \
    --ProjectId 1 \
    --ScriptContent print(1) \
    --ScriptName PYTHON2 \
    --ScriptPath 字符串 \
    --GroupId 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "77d45951-2edb-438c-9766-ef9551b1849b",
        "Record": {
            "Id": 909,
            "InstanceId": "20220223194219292_2022-03-02T23:15:59+08:00",
            "ScriptContent": "print(1)",
            "CreateTime": "2022-03-02T23:15:59+08:00",
            "Status": null
        },
        "Details": [
            {
                "Id": 909,
                "ScriptContent": "print(1)",
                "StartTime": null,
                "EndTime": null,
                "Status": "CREATED",
                "RecordId": 909
            }
        ]
    }
}
```

