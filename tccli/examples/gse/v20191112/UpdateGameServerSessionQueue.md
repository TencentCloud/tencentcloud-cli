**Example 1: 修改游戏服务器会话队列**



Input: 

```
tccli gse UpdateGameServerSessionQueue --cli-unfold-argument  \
    --Name queue2
```

Output: 
```
{
    "Response": {
        "GameServerSessionQueue": {
            "Destinations": [],
            "GameServerSessionQueueArn": "qcs::gse:ap-shanghai:uin/20555599:queue/queue2",
            "Name": "queue2",
            "PlayerLatencyPolicies": [],
            "TimeoutInSeconds": 600
        },
        "RequestId": "4e958efc-79af-47e4-9521-7744af034534c6a"
    }
}
```

