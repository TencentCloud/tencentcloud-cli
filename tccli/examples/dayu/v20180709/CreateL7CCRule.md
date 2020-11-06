**Example 1: 查询7层CC的访问频控自定义规则**



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

