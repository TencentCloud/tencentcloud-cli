**Example 1: 开启匹配返回示例**



Input: 

```
tccli gpm StartMatching --cli-unfold-argument  \
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
    --Players.0.RegionLatencies.0.Latency 100
```

Output: 
```
{
    "Response": {
        "ErrCode": 0,
        "MatchTicketId": "match_ticket_id",
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

