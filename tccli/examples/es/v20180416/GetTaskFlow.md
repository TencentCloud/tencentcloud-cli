**Example 1: 获取实例任务流程信息**

通过集群名和流程ID查流程运行状态

Input: 

```
tccli es GetTaskFlow --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --FlowId 33783
```

Output: 
```
{
    "Response": {
        "InstanceId": "es-xxxxxxxx",
        "TaskFlow": {
            "Id": 33783,
            "Status": 2
        },
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

