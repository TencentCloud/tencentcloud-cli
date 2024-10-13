**Example 1: 创建文本检索视频任务**

创建文本检索视频任务

Input: 

```
tccli mps CreateVideoSearchTask --cli-unfold-argument  \
    --SearchValueInput.SearchValueType Text \
    --SearchValueInput.TextInput 喜欢 \
    --Limit 3 \
    --TaskNotifyConfig.NotifyType URL \
    --TaskNotifyConfig.NotifyUrl http://qq.com/callback
```

Output: 
```
{
    "Response": {
        "TaskId": "251xxx279-SearchTask-60e4ae3b23ff4fd3936eb6b7e8af25ec",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

