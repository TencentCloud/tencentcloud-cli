**Example 1: 搜索游戏会话列表-creationTimeMillis条件**

搜索指定时间创建的游戏会话
creationTimeMillis=1575518668000，时间为创建游戏会话的UTC时间，单位：毫秒。
条件表达式：
FilterExpression: creationTimeMillis=1575518668000

Input: 

```
tccli gse SearchGameServerSessions --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-b1adh8hq \
    --Limit 1 \
    --NextToken nextToken-4hpp445-niuu789 \
    --FilterExpression creationTimeMillis%3d1575518668000 \
    --SortExpression creationTimeMillis+ASC
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
                "GameProperties": [
                    {
                        "Key": "Key-2aa06131-7d54-11ea-b3e7-3464a91513fe",
                        "Value": "Value-2aa06132-7d54-11ea-8199-3464a91513fe"
                    },
                    {
                        "Key": "Key-2aa06133-7d54-11ea-aaac-3464a91513fe",
                        "Value": "Value-2aa06134-7d54-11ea-8fa2-3464a91513fe"
                    },
                    {
                        "Key": "Key-2aa06135-7d54-11ea-a9c1-3464a91513fe",
                        "Value": "Value-2aa06136-7d54-11ea-b30b-3464a91513fe"
                    }
                ],
                "GameServerSessionData": "",
                "GameServerSessionId": "qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-111222",
                "AvailabilityStatus": "ENABLE",
                "InstanceType": "S5.SMALL2",
                "IpAddress": "0000.0.0.0",
                "MatchmakerData": "",
                "MaximumPlayerSessionCount": "10",
                "Name": "game-session-name",
                "PlayerSessionCreationPolicy": "ACCEPT_ALL",
                "Port": "8000",
                "Status": "ACTIVE",
                "StatusReason": "",
                "TerminationTime": "2019-12-05T04:04:28Z",
                "CurrentCustomCount": 0,
                "MaxCustomCount": 10,
                "Weight": 5
            }
        ],
        "NextToken": "",
        "RequestId": "0fffff4-oooo-43333d-9222-testaaa"
    }
}
```

**Example 2: 搜索游戏会话列表-游戏属性**

查询游戏属性Key-2aa06135-7d54-11ea-a9c1-3464a91513的值是Value-2aa06136-7d54-11ea-b30b-3464a91513fe游戏会话列表
条件表达式：
FilterExpression: gameServerSessionProperties.Key-2aa06135-7d54-11ea-a9c1-3464a91513fe=Value-2aa06136-7d54-11ea-b30b-3464a91513fe

Input: 

```
tccli gse SearchGameServerSessions --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-b1adh8hq \
    --Limit 1 \
    --NextToken nextToken-4hpp445-niuu789 \
    --FilterExpression gameServerSessionProperties.Key-2aa06135-7d54-11ea-a9c1-3464a91513fe%3dValue-2aa06136-7d54-11ea-b30b-3464a91513fe \
    --SortExpression creationTimeMillis+ASC
```

Output: 
```
{
    "Response": {
        "GameServerSessions": [
            {
                "AvailabilityStatus": "Unknown",
                "CreationTime": "2020-04-13T06:58:27Z",
                "CreatorId": "",
                "CurrentCustomCount": 0,
                "CurrentPlayerSessionCount": 0,
                "DnsName": "",
                "FleetId": "fleet-qp3g3caa-b1adh8hq",
                "GameProperties": [
                    {
                        "Key": "Key-2aa06131-7d54-11ea-b3e7-3464a91513fe",
                        "Value": "Value-2aa06132-7d54-11ea-8199-3464a91513fe"
                    },
                    {
                        "Key": "Key-2aa06133-7d54-11ea-aaac-3464a91513fe",
                        "Value": "Value-2aa06134-7d54-11ea-8fa2-3464a91513fe"
                    },
                    {
                        "Key": "Key-2aa06135-7d54-11ea-a9c1-3464a91513fe",
                        "Value": "Value-2aa06136-7d54-11ea-b30b-3464a91513fe"
                    }
                ],
                "GameServerSessionData": "",
                "GameServerSessionId": "qcs::gse:ap-shanghai:uin/0:gameserversession/fleet-qp3g3caa-b1adh8hq/gssess-k17ia36c-omi2numy",
                "InstanceType": "S5.SMALL2",
                "IpAddress": "200.0.0.1",
                "MatchmakerData": "",
                "MaxCustomCount": 0,
                "MaximumPlayerSessionCount": 78,
                "Name": "GameServerSessionName-2aa06130-7d54-11ea-9263-3464a91513fe",
                "PlayerSessionCreationPolicy": "ACCEPT_ALL",
                "Port": 59920,
                "Status": "ACTIVE",
                "StatusReason": "",
                "TerminationTime": null,
                "Weight": 0
            }
        ],
        "NextToken": "ntoken-bldnitiu-4cnjt4c0",
        "RequestId": "s1587465032390722054"
    }
}
```

**Example 3: 搜索游戏会话列表-复杂条件表达式**

条件表达式：
FilterExpression:
(maximumSessions>=10 OR playerSessionCount=0) OR NOT (creationTimeMillis>1575518668000) OR (maximumSessions>=10 AND hasAvailablePlayerSessions=true)

Input: 

```
tccli gse SearchGameServerSessions --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-b1adh8hq \
    --Limit 1 \
    --NextToken nextToken-4hpp445-niuu789 \
    --FilterExpression (maximumSessions%3e%3d10+OR+playerSessionCount%3d0)+OR+NOT+(creationTimeMillis%3e1575518668000)+OR+(maximumSessions%3e%3d10+AND+hasAvailablePlayerSessions%3dtrue) \
    --SortExpression creationTimeMillis+ASC
```

Output: 
```
{
    "Response": {
        "GameServerSessions": [
            {
                "AvailabilityStatus": "Unknown",
                "CreationTime": "2020-04-13T06:58:07Z",
                "CreatorId": "",
                "MaxCustomCount": 0,
                "CurrentCustomCount": 0,
                "CurrentPlayerSessionCount": 0,
                "DnsName": "",
                "FleetId": "fleet-qp3g3caa-b1adh8hq",
                "GameProperties": [
                    {
                        "Key": "Key-1ea66e9e-7d54-11ea-a4aa-3464a91513fe",
                        "Value": "Value-1ea66e9f-7d54-11ea-a71e-3464a91513fe"
                    },
                    {
                        "Key": "Key-1ea66ea0-7d54-11ea-9afd-3464a91513fe",
                        "Value": "Value-1ea66ea1-7d54-11ea-a5f2-3464a91513fe"
                    },
                    {
                        "Key": "Key-1ea66ea2-7d54-11ea-b184-3464a91513fe",
                        "Value": "Value-1ea66ea3-7d54-11ea-b355-3464a91513fe"
                    }
                ],
                "GameServerSessionData": "",
                "GameServerSessionId": "qcs::gse:ap-shanghai:uin/0:gameserversession/fleet-qp3g3caa-b1adh8hq/gssess-k17ia36c-2hs38yc0",
                "InstanceType": "S5.SMALL2",
                "IpAddress": "200.0.0.2",
                "MatchmakerData": "",
                "MaximumPlayerSessionCount": 181,
                "Name": "GameServerSessionName-1ea66e9d-7d54-11ea-b041-3464a91513fe",
                "PlayerSessionCreationPolicy": "ACCEPT_ALL",
                "Port": 59106,
                "Status": "ACTIVE",
                "StatusReason": "",
                "TerminationTime": null,
                "Weight": 0
            },
            {
                "AvailabilityStatus": "Unknown",
                "CreationTime": "2020-04-13T07:49:16Z",
                "CreatorId": "",
                "CurrentCustomCount": 0,
                "CurrentPlayerSessionCount": 0,
                "DnsName": "",
                "FleetId": "fleet-qp3g3caa-b1adh8hq",
                "GameProperties": [],
                "GameServerSessionData": "",
                "GameServerSessionId": "qcs::gse:ap-shanghai:uin/0:gameserversession/fleet-qp3g3caa-b1adh8hq/gssess-k17ia36c-oik1x49i",
                "InstanceType": "S5.SMALL2",
                "IpAddress": "200.0.0.1",
                "MatchmakerData": "",
                "MaxCustomCount": 0,
                "MaximumPlayerSessionCount": 200,
                "Name": "GameServerSessionName-45bd031c-7d5b-11ea-acf8-52540024df83",
                "PlayerSessionCreationPolicy": "ACCEPT_ALL",
                "Port": 59110,
                "Status": "ACTIVE",
                "StatusReason": "",
                "TerminationTime": null,
                "Weight": 0
            }
        ],
        "NextToken": "ntoken-bldnitiu-4cnjt4c0",
        "RequestId": "s1587466067806554523"
    }
}
```

