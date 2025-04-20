**Example 1: 仅查看默认场景**

仅查看默认场景

Input: 

```
tccli waf DescribeBotSceneList --cli-unfold-argument  \
    --Domain fgsta.qcloudwaf.com \
    --Limit 10 \
    --BusinessType all \
    --IsDefault true \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d399557f-0050-4402-adb6-d0af24671738",
        "BotSceneList": [
            {
                "SceneId": "3000004602",
                "Type": "default",
                "SceneName": "默认场景",
                "UpdateTime": 1666262225512,
                "BusinessType": [],
                "ClientType": [
                    "browser"
                ],
                "Priority": 100,
                "MatchCondition": [],
                "MatchType": "",
                "ActionMatchType": "and",
                "SceneStatus": true,
                "JsInjectStatus": false,
                "AIStatus": true,
                "TIStatus": true,
                "StatisticStatus": false,
                "ActionRuleCount": 1,
                "UCBCount": 0,
                "UAStatus": true
            }
        ],
        "TotalCount": 1,
        "SimpleFlag": true
    }
}
```

