**Example 1: 示例**



Input: 

```
tccli wedata BatchCreateTaskVersionAsync --cli-unfold-argument  \
    --Tasks.0.TaskId 20250227112817430 \
    --Tasks.0.VersionRemark 备注 \
    --AutoRun True \
    --AlarmWays true \
    --AlarmRecipientTypes all \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "2c66cc14-ea0a-4f25-bb2c-3a315bd9b606"
    }
}
```

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata BatchCreateTaskVersionAsync --cli-unfold-argument  \
    --Tasks.0.TaskId 20230425181533351 \
    --Tasks.0.VersionRemark ces \
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

