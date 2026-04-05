**Example 1: ListNotifications**

查询工作空间通知列表

Input: 

```
tccli wedata ListNotifications --cli-unfold-argument  \
    --WorkspaceId 1 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 5 \
    --Keywords wedhook
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ChannelType": 2,
                    "EmailAddress": "",
                    "Name": "wedhook",
                    "NotificationId": "0",
                    "Password": "",
                    "Url": "http://baidu.com",
                    "Username": "",
                    "WorkspaceId": "1"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 5,
                "TotalCount": 1,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "77eb4d1f-3039-4abb-a7a6-606cc7acd76e"
    }
}
```

