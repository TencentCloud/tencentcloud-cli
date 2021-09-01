**Example 1: 获取游戏会话详情列表**

获取游戏会话详情列表

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
                "ProtectionPolicy": "TimeLimitProtection"
            }
        ],
        "NextToken": "",
        "RequestId": "0a6ce70b-ffc8-4b9a-9255-d1915test"
    }
}
```

