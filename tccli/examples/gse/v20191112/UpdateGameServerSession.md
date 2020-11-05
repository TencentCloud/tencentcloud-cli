**Example 1: Updating game session attributes**

This example shows you how to update the attributes of a game session.

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
            "CreationTime": "2019-12-06T10:03:50Z",
            "CreatorId": "c1",
            "CurrentPlayerSessionCount": 1,
            "DnsName": "",
            "FleetId": "fleet-00test-a5testzz",
            "GameProperties": [],
            "GameServerSessionData": "testdata",
            "GameServerSessionId": "qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde",
            "IpAddress": "0000.0.0.0",
            "MatchmakerData": "",
            "MaximumPlayerSessionCount": 10,
            "Name": "",
            "PlayerSessionCreationPolicy": "ACCEPT_ALL",
            "Port": 8000,
            "Status": "ACTIVE",
            "StatusReason": "",
            "TerminationTime": "2019-12-06T11:33:10Z"
        },
        "RequestId": "0fffff4-oooo-43333d-9222-testaaa"
    }
}
```

