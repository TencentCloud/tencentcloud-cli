**Example 1: 调试运行集成任务**

调试运行集成任务

Input: 

```
tccli wedata DryRunDIOfflineTask --cli-unfold-argument  \
    --TaskId 446569620893696 \
    --ResourceGroup mysql \
    --ProjectId 1486446569620893696 \
    --TaskTypeId 201
```

Output: 
```
{
    "Response": {
        "CurrentRunDate": "2022-04-12 17:00:15",
        "ProjectId": "1486446569620893696",
        "Status": "running",
        "TaskId": "446569620893696",
        "TaskInstanceKey": "64893b7dff394c353ae305796ba2",
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

