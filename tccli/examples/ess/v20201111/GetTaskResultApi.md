**Example 1: test示例**

通过转换任务Id查询任务状态

Input: 

```
tccli ess GetTaskResultApi --cli-unfold-argument  \
    --Operator.UserId yDxoQxxxxxxxxxxxxxxxxxx1h2hnnR \
    --TaskId 2022xxxxxxxxxx992850
```

Output: 
```
{
    "Response": {
        "RequestId": "2255xxxxx76-6192fc301053",
        "ResourceId": "yDRtsUxxxxxjEyx4jZM3A7",
        "TaskId": "2022072xxxx992850",
        "TaskMessage": "任务处理完成",
        "TaskStatus": 8
    }
}
```

