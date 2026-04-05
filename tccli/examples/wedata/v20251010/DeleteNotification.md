**Example 1: DeleteNotification**

工作空间删除通知

Input: 

```
tccli wedata DeleteNotification --cli-unfold-argument  \
    --NotificationId 784432457553612800 \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "92e3cedd-ed41-4e6b-807c-545aae40de8b"
    }
}
```

