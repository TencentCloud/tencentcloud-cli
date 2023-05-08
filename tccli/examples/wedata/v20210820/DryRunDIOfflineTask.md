**Example 1: 调试运行集成任务**

调试运行集成任务

Input: 

```
tccli wedata DryRunDIOfflineTask --cli-unfold-argument  \
    --TaskId xx \
    --ProjectId xx \
    --ResourceGroup xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "CurrentRunDate": "xx",
        "ProjectId": "xx",
        "Status": "xx",
        "TaskId": "xx",
        "TaskInstanceKey": "xx"
    }
}
```

