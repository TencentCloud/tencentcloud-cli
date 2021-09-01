**Example 1: 查询游戏服务器会话的放置**



Input: 

```
tccli gse DescribeGameServerSessionPlacement --cli-unfold-argument  \
    --PlacementId PlacementId-3a7d34cd-5240-11ea-b02a-3464sdf513fe
```

Output: 
```
{
    "Response": {
        "GameServerSessionPlacement": {
            "DnsName": "",
            "EndTime": "2020-02-18T11:27:23Z",
            "GameProperties": [
                {
                    "Key": "Key-3a7d34d0-5240-11ea-a3b0-3464afff13fe",
                    "Value": "Value-3a7d34d1-5240-11ea-9466-344654391513fe"
                }
            ],
            "GameServerSessionData": "GameServerSessionData-3a7d34d2-5240-11ea-8dd4-3464afdf1513fe",
            "GameServerSessionId": "",
            "GameServerSessionName": "GameServerSessionName-3a7d34d3-5240-11ea-8564-3464sd1513fe",
            "GameServerSessionQueueName": "PlacementTwo",
            "GameServerSessionRegion": "",
            "IpAddress": "",
            "MatchmakerData": "",
            "MaximumPlayerSessionCount": 100,
            "PlacedPlayerSessions": [],
            "PlacementId": "PlacementId-3a7d34cd-5240-11ea-b02a-3464sdf513fe",
            "PlayerLatencies": [
                {
                    "LatencyInMilliseconds": 10000,
                    "PlayerId": "Player-3a7d34d4-5240-11ea-a2ee-3464a91513fe",
                    "RegionIdentifier": "ap-shanghai"
                }
            ],
            "Port": 0,
            "StartTime": "2020-02-18T11:17:23Z",
            "Status": "TIMED_OUT"
        }
    }
}
```

