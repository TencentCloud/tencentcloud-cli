**Example 1: 查询云端审核任务信息**



Input: 

```
tccli trtc DescribeCloudModeration --cli-unfold-argument  \
    --SdkAppId 20010806 \
    --TaskId -nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ..
```

Output: 
```
{
    "Response": {
        "TaskId": "-npVoIhU7nVF+0aF9cAU08H4y253LKPbBX+UIoK-4pycoZWQndibGOPu9klhRT7bEDv5XoewCQE.",
        "Status": "InProgress",
        "RequestId": "uis_mock",
        "SubscribeStreamUserIds": {
            "SubscribeAudioUserIds": [],
            "UnSubscribeAudioUserIds": [],
            "SubscribeVideoUserIds": [],
            "UnSubscribeVideoUserIds": []
        }
    }
}
```

