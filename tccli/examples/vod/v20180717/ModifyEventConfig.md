**Example 1: 设置事件通知信息**



Input: 

```
tccli vod ModifyEventConfig --cli-unfold-argument  \
    --Mode PUSH \
    --NotificationUrl http://mydemo.com/receiveevent \
    --UploadMediaCompleteEventSwitch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

