**Example 1: 查询业务和攻击概要趋势**



Input: 

```
tccli waf DescribePeakPoints --cli-unfold-argument  \
    --FromTime 2021-07-21 00:00:00 \
    --ToTime 2021-07-21 23:59:59
```

Output: 
```
{
    "Response": {
        "Points": [
            {
                "Time": 1626908400,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908460,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908520,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908580,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908640,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908700,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908760,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908820,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908880,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626908940,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            },
            {
                "Time": 1626909000,
                "Access": 0,
                "BotAccess": 0,
                "Attack": 0,
                "Cc": 0,
                "Down": 0,
                "Up": 0,
                "StatusServerError": 1,
                "StatusClientError": 1,
                "StatusRedirect": 1,
                "StatusOk": 1,
                "UpstreamServerError": 1,
                "UpstreamClientError": 1,
                "UpstreamRedirect": 1
            }
        ],
        "RequestId": "fuqian-test"
    }
}
```

