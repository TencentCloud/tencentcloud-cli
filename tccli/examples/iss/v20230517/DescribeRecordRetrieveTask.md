**Example 1: 成功**

 

Input: 

```
tccli iss DescribeRecordRetrieveTask --cli-unfold-argument  \
    --TaskId d00a3e6f9b**********040cebcee7a6
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "d00a3e6f9b**********040cebcee7a6",
            "TaskName": "name",
            "StartTime": 1687688595,
            "EndTime": 1687692195,
            "Mode": 1,
            "Expiration": 3,
            "Status": 0,
            "Capacity": 10000,
            "Channels": [
                {
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "11",
                    "ChannelId": "32525dd7-c3fc-****-****-d5beb4acd1e1",
                    "ChannelName": "SDK-NVR05",
                    "Status": 0
                }
            ],
            "Describe": "abc",
            "ChannelCount": 1
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

