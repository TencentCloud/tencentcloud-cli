**Example 1: CreateNotification**

工作空间创建通知

Input: 

```
tccli wedata CreateNotification --cli-unfold-argument  \
    --ChannelType 2 \
    --WorkspaceId 1 \
    --Name webhook_123 \
    --EmailAddress None \
    --Url http://baidu.com \
    --Username None \
    --Password None
```

Output: 
```
{
    "Response": {
        "Data": {
            "NotificationId": "784432457553612800"
        },
        "RequestId": "9a30d3f4-0c64-48e7-bc6e-4e6d6e66a923"
    }
}
```

