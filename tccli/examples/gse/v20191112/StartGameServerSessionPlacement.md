**Example 1: 开始放置游戏服务器会话**



Input: 

```
tccli gse StartGameServerSessionPlacement --cli-unfold-argument  \
    --PlacementId PlacementId-3a7d34cd-5240-11ea-b02a-3464a91513fe \
    --GameServerSessionQueueName PlacementTwo \
    --MaximumPlayerSessionCount 100
```

Output: 
```
{
    "Response": {
        "GameServerSessionPlacement": {
            "DnsName": "",
            "EndTime": null,
            "GameProperties": [],
            "GameServerSessionData": "",
            "GameServerSessionId": "",
            "GameServerSessionName": "",
            "GameServerSessionQueueName": "PlacementTwo",
            "GameServerSessionRegion": "",
            "IpAddress": "",
            "MatchmakerData": "",
            "MaximumPlayerSessionCount": 100,
            "PlacedPlayerSessions": [],
            "PlacementId": "PlacementId-3a7d34cd-5240-11ea-b02a-3464a91513fe",
            "PlayerLatencies": [],
            "Port": 0,
            "StartTime": "2020-02-18T11:17:23Z",
            "Status": "PENDING"
        },
        "RequestId": "84708eb1-0247-43f8-834e-c7edfdsfdgd53"
    }
}
```

