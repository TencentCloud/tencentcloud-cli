**Example 1: 停止放置游戏服务器会话**



Input: 

```
tccli gse StopGameServerSessionPlacement --cli-unfold-argument  \
    --PlacementId PlacementId-3a7d34cd-5240-11ea-b02a-3464sdfsfsdf13fe
```

Output: 
```
{
    "Response": {
        "GameServerSessionPlacement": {
            "DnsName": "",
            "EndTime": "2020-02-18T11:33:49Z",
            "GameProperties": [
                {
                    "Key": "Key-8658b11f-5242-11ea-9c67-3464a435513fe",
                    "Value": "Value-8658b120-5242-11ea-8527-34t4a91513fe"
                }
            ],
            "GameServerSessionData": "GameServerSessionData-8658b121-5242-11ea-af53-34644351513fe",
            "GameServerSessionId": "",
            "GameServerSessionName": "GameServerSessionName-8658b122-5242-11ea-9f8f-3464491513fe",
            "GameServerSessionQueueName": "PlacementTwo",
            "GameServerSessionRegion": "",
            "IpAddress": "",
            "MatchmakerData": "",
            "MaximumPlayerSessionCount": 100,
            "PlacedPlayerSessions": [],
            "PlacementId": "PlacementId-3a7d34cd-5240-11ea-b02a-3464sdfsfsdf13fe",
            "PlayerLatencies": [
                {
                    "LatencyInMilliseconds": 10000,
                    "PlayerId": "Player-8658b123-5242-11ea-9e2f-3464sf91513fe",
                    "RegionIdentifier": "ap-shanghai"
                }
            ],
            "Port": 0,
            "StartTime": "2020-02-18T11:33:49Z",
            "Status": "CANCELLED"
        },
        "RequestId": "2f631834-4c91-4c9b-a13a-2d5757582eb5f"
    }
}
```

