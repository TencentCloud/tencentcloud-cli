**Example 1: 开发空间获取最近一次测试运行记录信息**

开发空间获取最近一次测试运行记录信息

Input: 

```
tccli wedata GetLatestAnalyseInfo --cli-unfold-argument  \
    --ProjectId abc \
    --ScriptId abc \
    --IsOnlyCurrUser True
```

Output: 
```
{
    "Response": {
        "ProjectId": "abc",
        "Task": {
            "TaskId": "abc",
            "RecordId": "abc",
            "CurRunDate": "abc",
            "RequestScriptId": "abc",
            "TaskStatus": "abc",
            "CreateUser": "abc",
            "ProjectId": "abc"
        },
        "RequestId": "abc"
    }
}
```

