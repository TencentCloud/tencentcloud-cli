**Example 1: 查询玩家会话列表**

查询玩家会话列表

Input: 

```
tccli gse DescribePlayerSessions --cli-unfold-argument  \
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde \
    --Limit 5 \
    --NextToken nextToken-abc78-1122bc
```

Output: 
```
{
    "Response": {
        "NextToken": "nextToken-4hpp445-niuu789",
        "PlayerSessions": [
            {
                "CreationTime": "2019-12-06T11:33:19Z",
                "DnsName": "",
                "FleetId": "fleet-00test-a5testzz",
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

