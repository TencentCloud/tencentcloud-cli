**Example 1: 查询开发空间sql任务试运行子实例列表**

查询开发空间sql任务试运行子实例列表

Input: 

```
tccli wedata DescribeDrSonInstance --cli-unfold-argument  \
    --ProjectId abc \
    --TaskSource abc \
    --RecordId 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
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
            }
        ],
        "RequestId": "abc"
    }
}
```

