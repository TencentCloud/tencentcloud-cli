**Example 1: 查询试运行实例执行的脚本内容**

查询试运行实例执行的脚本内容

Input: 

```
tccli wedata DescribeDrInstanceScriptContent --cli-unfold-argument  \
    --ProjectId abc \
    --TaskSource abc \
    --RecordId 1 \
    --SonRecordId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskSource": "abc",
            "RecordId": 1,
            "SonRecordId": 1,
            "InstanceId": "abc",
            "TaskId": "abc",
            "ScriptContent": "abc",
            "CreateTime": "abc",
            "StartTime": "abc",
            "Duration": "abc",
            "Status": "abc",
            "TaskName": "abc",
            "SubmitUserName": "abc",
            "SubmitUserId": "abc",
            "TaskType": "abc",
            "HasResultSet": true
        },
        "RequestId": "abc"
    }
}
```

