**Example 1: Getting the list of game session details**

This example shows you how to get the list of game session details.

Input: 

```
tccli gse DescribeGameServerSessionDetails --cli-unfold-argument  \
    --FleetId fleet-test00-1223 \
    --Limit 5 \
    --NextToken nextToken-test01-tt
```

Output: 
```
{
    "Response": {
        "GameServerSessionDetails": [
            {
                "GameServerSession": {
                    "CreationTime": "2019-12-06T10:03:50Z",
                    "CreatorId": "c1",
                    "CurrentPlayerSessionCount": 0,
                    "DnsName": "",
                    "FleetId": "fleet-pro4extc-f1hiuzry",
                    "GameProperties": [],
                    "GameServerSessionData": "testdata",
                    "GameServerSessionId": "qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde",
                    "IpAddress": "0000.0.0.0",
                    "MatchmakerData": "",
                    "MaximumPlayerSessionCount": 10,
                    "Name": "",
                    "PlayerSessionCreationPolicy": "ACCEPT_ALL",
                    "Port": 8000,
                    "Status": "TERMINATED",
                    "StatusReason": "",
                    "TerminationTime": "2019-12-08T02:53:27Z"
                },
                "ProtectionPolicy": "FullProtection"
            }
        ],
        "NextToken": "",
        "RequestId": "0a6ce70b-ffc8-4b9a-9255-d1915test"
    }
}
```

