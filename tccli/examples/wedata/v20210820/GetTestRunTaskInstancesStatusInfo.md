**Example 1: 获取调试任务实例状态信息**

获取调试任务实例状态信息

Input: 

```
tccli wedata GetTestRunTaskInstancesStatusInfo --cli-unfold-argument  \
    --Tasks.0.RecordId abc \
    --IsDevSpace False
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "InstanceId": "abc",
                "Status": "abc",
                "RecordId": "abc",
                "TaskId": "abc"
            }
        ],
        "Messages": "abc",
        "IsException": true,
        "RequestId": "abc"
    }
}
```

