**Example 1: 创建单个玩家会话**

创建单个玩家会话

Input: 

```
tccli gse JoinGameServerSession --cli-unfold-argument  \
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde \
    --PlayerData testData \
    --PlayerId testPlayer
```

Output: 
```
{
    "Response": {
        "PlayerSession": {
            "CreationTime": "2019-12-05T15:15:33Z",
            "DnsName": "",
            "FleetId": "fleet-sss-test01",
            "GameServerSessionId": "qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde",
            "IpAddress": "0000.0.0.0",
            "PlayerData": "imangozhang",
            "PlayerId": "100",
            "PlayerSessionId": "psess-d44990-test5",
            "Port": "8000",
            "Status": "RESERVED",
            "TerminationTime": null
        },
        "RequestId": "0fffff4-oooo-43333d-9222-testaaa"
    }
}
```

