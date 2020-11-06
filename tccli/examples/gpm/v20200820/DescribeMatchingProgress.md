**Example 1: 获取匹配进度信息示例**



Input: 

```
tccli gpm DescribeMatchingProgress --cli-unfold-argument  \
    --MatchTicketIds.0.MatchCode match-lipp \
    --MatchTicketIds.0.MatchTicketId ml0urJm
```

Output: 
```
{
    "Response": {
        "ErrCode": 0,
        "MatchTickets": [
            {
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
            }
        ],
        "RequestId": "1a68664b-d796-407b-ab7b-2dbc2a12f8f5"
    }
}
```

