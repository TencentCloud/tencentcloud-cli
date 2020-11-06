**Example 1: 创建游戏服务会话**

创建游戏服务会话

Input: 

```
tccli gse CreateGameServerSession --cli-unfold-argument  \
    --AliasId alias-aatest-66bb \
    --MaximumPlayerSessionCount 10
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

