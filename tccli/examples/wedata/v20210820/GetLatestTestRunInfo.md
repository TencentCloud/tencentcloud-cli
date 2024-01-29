**Example 1: 编排空间获取最近一次测试运行记录信息**

编排空间获取最近一次测试运行记录信息

Input: 

```
tccli wedata GetLatestTestRunInfo --cli-unfold-argument  \
    --ProjectId abc \
    --TaskIds abc \
    --IsOnlyCurrUser True
```

Output: 
```
{
    "Response": {
        "ProjectId": "abc",
        "Tasks": [
            {
                "TaskId": "abc",
                "RecordId": "abc",
                "CurRunDate": "abc",
                "RequestTaskId": "abc",
                "TaskStatus": "abc",
                "JobId": "abc",
                "CreateUser": "abc",
                "ProjectId": "abc",
                "SerialNo": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

