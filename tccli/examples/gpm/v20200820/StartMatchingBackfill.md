**Example 1: 开启回填匹配返回示例**



Input: 

```
tccli gpm StartMatchingBackfill --cli-unfold-argument  \
    --MatchCode match_code \
    --MatchTicketId match_ticket_id \
    --Players.0.Id player_id_0 \
    --Players.0.Name player_name \
    --Players.0.Team player_team \
    --Players.0.CustomPlayerStatus 0 \
    --Players.0.CustomProfile player_custom_profile \
    --Players.0.MatchAttributes.0.Name player_match_attributes_name \
    --Players.0.MatchAttributes.0.Type 0 \
    --Players.0.MatchAttributes.0.NumberValue 10 \
    --Players.0.RegionLatencies.0.Region ap-shanghai \
    --Players.0.RegionLatencies.0.Latency 100 \
    --GameServerSessionId game_server_session_id
```

Output: 
```
{
    "Response": {
        "MatchTicket": {
            "EndTime": "",
            "Id": "ml0urJm",
            "MatchCode": "match-lipp",
            "MatchResult": "",
            "MatchType": "",
            "Players": [
                {
                    "CustomPlayerStatus": 0,
                    "CustomProfile": "",
                    "Id": "fisher0",
                    "MatchAttributes": [
                        {
                            "ListValue": [],
                            "MapValue": [],
                            "Name": "numberAttr",
                            "NumberValue": 10,
                            "StringValue": "",
                            "Type": 0
                        },
                        {
                            "ListValue": [],
                            "MapValue": [],
                            "Name": "stringAttr",
                            "NumberValue": 0,
                            "StringValue": "stringAttrVal",
                            "Type": 1
                        },
                        {
                            "ListValue": [
                                "listAttrVal1",
                                "listAttrVal2",
                                "listAttrVal3"
                            ],
                            "MapValue": [],
                            "Name": "listAttr",
                            "NumberValue": 0,
                            "StringValue": "",
                            "Type": 2
                        },
                        {
                            "ListValue": [],
                            "MapValue": [
                                {
                                    "Key": "mapAttrVal1",
                                    "Value": 10
                                },
                                {
                                    "Key": "mapAttrVal2",
                                    "Value": 20
                                },
                                {
                                    "Key": "mapAttrVal3",
                                    "Value": 30
                                }
                            ],
                            "Name": "mapAttr",
                            "NumberValue": 0,
                            "StringValue": "",
                            "Type": 3
                        }
                    ],
                    "Name": "playerName0",
                    "RegionLatencies": [
                        {
                            "Latency": 100,
                            "Region": "ap-guangzhou"
                        },
                        {
                            "Latency": 100,
                            "Region": "ap-beijing"
                        }
                    ],
                    "Team": "playerTeam0"
                }
            ],
            "StartTime": "2020-09-05T11:11:15Z",
            "Status": "TIMEDOUT",
            "StatusMessage": "",
            "StatusReason": ""
        },
        "RequestId": "1a68664b-d796-407b-ab7b-2dbc2a12f8f5"
    }
}
```

