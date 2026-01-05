**Example 1: sample**



Input: 

```
tccli waf DescribeBotIdRule --cli-unfold-argument  \
    --Domain admin.com \
    --SceneId 303242221 \
    --RuleId 333242221 \
    --BotId emptyua \
    --Level 100 \
    --BotIdType ddos \
    --Status 0 \
    --RuleAction monitor
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RuleId": "333242221",
                "BotId": "emptyua",
                "Status": true,
                "Action": "monitor",
                "Level": 100,
                "BotIdType": "ddos",
                "ModifyTime": 0,
                "InsertTime": 0,
                "Description": "miaoshuxinxi",
                "Influence": "high"
            }
        ],
        "TotalCount": 10,
        "StatInfo": {
            "Pattern": "intercept",
            "TotalCount": 0,
            "MonitorCount": 0,
            "InterceptCount": 10
        },
        "RequestId": "req-id-23112"
    }
}
```

