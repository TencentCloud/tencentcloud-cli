**Example 1: 创建一组玩家会话**

创建一组玩家会话

Input: 

```
tccli gse JoinGameServerSessionBatch --cli-unfold-argument  \
    --PlayerIds xx \
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde \
    --PlayerDataMap.Value xx \
    --PlayerDataMap.Key xx
```

Output: 
```
{
    "Response": {
        "PlayerSessions": [
            {
                "CreationTime": "2019-12-06T11:33:19Z",
                "DnsName": "",
                "FleetId": "fleet-ptest40-f001",
                "GameServerSessionId": "qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde",
                "IpAddress": "0000.0.0.0",
                "PlayerData": "TestPlayerData",
                "PlayerId": "",
                "PlayerSessionId": "psess-d44990-test5",
                "Port": 8000,
                "Status": "COMPLETED",
                "TerminationTime": "2019-12-06T11:33:18Z"
            }
        ],
        "RequestId": "0fffff4-oooo-43333d-9222-testaaa"
    }
}
```

