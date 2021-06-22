**Example 1: 创建游戏服务器会话队列**



Input: 

```
tccli gse CreateGameServerSessionQueue --cli-unfold-argument  \
    --Name test
```

Output: 
```
{
    "Response": {
        "GameServerSessionQueue": {
            "Destinations": [],
            "GameServerSessionQueueArn": "qcs::gse:ap-shanghai:uin/20534889:queue/test",
            "Name": "test",
            "PlayerLatencyPolicies": [],
            "TimeoutInSeconds": 600,
            "Tags": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ]
        },
        "RequestId": "08f383c1-2694-4236-ba64-e7d3e3453d96c"
    }
}
```

