**Example 1: Creating game server session**

This example shows you how to create a game server session.

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
            "CreationTime": "2019-12-05T04:08:29Z",
            "CreatorId": "c2",
            "CurrentPlayerSessionCount": "0",
            "DnsName": "",
            "FleetId": "fleet-test01",
            "GameProperties": [],
            "GameServerSessionData": "test",
            "GameServerSessionId": "qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde",
            "IpAddress": "0000.0.0.0",
            "MatchmakerData": "",
            "MaximumPlayerSessionCount": "10",
            "Name": "",
            "PlayerSessionCreationPolicy": "ACCEPT_ALL",
            "Port": "8000",
            "Status": "ACTIVATING",
            "StatusReason": "",
            "TerminationTime": null
        },
        "RequestId": "s1-test-requestid01"
    }
}
```

