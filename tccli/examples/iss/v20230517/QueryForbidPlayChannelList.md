**Example 1: 查询禁播列表**



Input: 

```
tccli iss QueryForbidPlayChannelList --cli-unfold-argument  \
    --UserId 10********82 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ChannelId": "32525dd7-c3fc-****-****-d5beb4acd1e1",
                    "ChannelName": "11",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 1
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

