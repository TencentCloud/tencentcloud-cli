**Example 1: 调试运行集成任务**

调试运行集成任务

Input: 

```
tccli wedata DryRunDIOfflineTask --cli-unfold-argument  \
    --TaskId abc \
    --ResourceGroup abc \
    --ProjectId abc \
    --TaskTypeId 1
```

Output: 
```
{
    "Response": {
        "CurrentRunDate": "abc",
        "ProjectId": "abc",
        "Status": "abc",
        "TaskId": "abc",
        "TaskInstanceKey": "abc",
        "RequestId": "abc"
    }
}
```

