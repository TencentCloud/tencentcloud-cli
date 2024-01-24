**Example 1: 示例**



Input: 

```
tccli wedata BatchCreateTaskVersionAsync --cli-unfold-argument  \
    --Tasks.0.TaskId abc \
    --Tasks.0.VersionRemark abc \
    --AutoRun True \
    --AlarmWays abc \
    --AlarmRecipientTypes abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata BatchCreateTaskVersionAsync --cli-unfold-argument  \
    --Tasks.0.TaskId 20230425181533351 \
    --Tasks.0.VersionRemark 1111 \
    --AutoRun True \
    --AlarmWays email \
    --AlarmRecipientTypes 2 \
    --ProjectId 1470561602745229312
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "操作失败"
        },
        "RequestId": "6218d665-282f-4e43-972a-262dc311618e"
    }
}
```

