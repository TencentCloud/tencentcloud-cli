**Example 1: UpdateNotification**

工作空间修改通知

Input: 

```
tccli wedata UpdateNotification --cli-unfold-argument  \
    --ChannelType 2 \
    --WorkspaceId 1 \
    --NotificationId 784432457553612800 \
    --Name webhook_2025 \
    --EmailAddress None \
    --Url None \
    --Username None \
    --Password None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "a59c47cf-0bef-4aeb-b492-d9e139244476"
    }
}
```

