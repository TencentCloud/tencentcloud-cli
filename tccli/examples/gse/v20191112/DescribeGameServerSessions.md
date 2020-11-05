**Example 1: Querying game session list**

This example shows you how to query the list of game sessions.

Input: 

```
tccli gse DescribeGameServerSessions --cli-unfold-argument  \
    --AliasId a\
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-111222\
    --Limit 1\
    --NextToken nextToken-4hpp445-niuu789\
    --StatusFilter ACTIVATING
```

Output: 
```
{
    "Response": {
        "GameServerSessions": [
            {
                "CreationTime": "2019-12-05T12:04:28Z",
                "CreatorId": "c2",
                "CurrentPlayerSessionCount": "0",
                "DnsName": "",
                "FleetId": "fleet-00test-a5testzz",
                "GameProperties": [],
                "GameServerSessionData": "",
                "GameServerSessionId": "qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-111222",
                "IpAddress": "0000.0.0.0",
                "MatchmakerData": "",
                "MaximumPlayerSessionCount": "10",
                "Name": "",
                "PlayerSessionCreationPolicy": "ACCEPT_ALL",
                "Port": "8000",
                "Status": "ACTIVATING",
                "StatusReason": "",
                "TerminationTime": "2019-12-05T04:04:28Z"
            }
        ],
        "NextToken": "",
        "RequestId": "0fffff4-oooo-43333d-9222-testaaa"
    }
}
```

