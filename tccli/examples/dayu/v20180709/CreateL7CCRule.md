**Example 1: Querying custom layer-7 CC access frequency control rule**



Input: 

```
tccli dayu CreateL7CCRule --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleId rule-00000001 \
    --Method query
```

Output: 
```
{
    "Response": {
        "RequestId": "07efcf74-79b1-4faa-a61e-ec9310675b67",
        "RuleConfig": [
            {
                "Period": 60,
                "ReqNumber": 1,
                "Action": "drop",
                "ExeDuration": 1
            }
        ]
    }
}
```

