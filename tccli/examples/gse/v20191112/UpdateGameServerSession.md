**Example 1: 更新游戏会话属性**

更新游戏会话属性

Input: 

```
tccli gse UpdateGameServerSession --cli-unfold-argument  \
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde
```

Output: 
```
{
    "Response": {
        "GameServerSession": {
            "AvailabilityStatus": "Enable",
            "CreationTime": "2020-07-30T03:55:43Z",
            "CreatorId": "",
            "CurrentCustomCount": 0,
            "CurrentPlayerSessionCount": 0,
            "DnsName": "",
            "FleetId": "fleet-qp33caaa-35555",
            "GameProperties": [],
            "GameServerSessionData": "",
            "GameServerSessionId": "qcs::gse:ap-shanghai:uin/100000010000:gameserversession/fleet-qp33caaa-35555/gssess-qtk2222-uuu",
            "InstanceType": "S5.LARGE8",
            "IpAddress": "127.0.0.1",
            "MatchmakerData": "",
            "MaxCustomCount": 0,
            "MaximumPlayerSessionCount": 100,
            "Name": "",
            "PlayerSessionCreationPolicy": "ACCEPT_ALL",
            "Port": 6000,
            "Status": "ACTIVATING",
            "StatusReason": "",
            "TerminationTime": null,
            "Weight": 5
        },
        "RequestId": "s15960816666663333"
    }
}
```

