**Example 1: 全局UCB列表**

全局UCB列表

Input: 

```
tccli waf DescribeBotSceneUCBRule --cli-unfold-argument  \
    --Sort timestamp:-1 \
    --Skip 0 \
    --Domain fgsta.qcloudwaf.com \
    --Limit 2 \
    --SceneId global
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "Domain": "admin.com",
                    "Name": "custom-1",
                    "Rule": [
                        {
                            "Key": "url",
                            "Op": "eq",
                            "Value": {
                                "BasicValue": "/login",
                                "LogicValue": true,
                                "BelongValue": [
                                    "/login"
                                ],
                                "ValidKey": "url",
                                "MultiValue": [
                                    "/login"
                                ]
                            },
                            "OpOp": "rematch",
                            "OpArg": [
                                "name"
                            ],
                            "OpValue": 0,
                            "Name": "age"
                        }
                    ],
                    "Action": "monitor",
                    "OnOff": "on",
                    "RuleType": 0,
                    "Prior": 0,
                    "Timestamp": 0,
                    "Label": "human",
                    "Id": "3021313",
                    "SceneId": "3021312412",
                    "ValidTime": 0,
                    "Appid": 1,
                    "AdditionArg": "none",
                    "Desc": "none",
                    "RuleId": "320032232",
                    "PreDefine": true,
                    "JobType": "hour",
                    "JobDateTime": {
                        "Timed": [
                            {
                                "StartDateTime": 1,
                                "EndDateTime": 1
                            }
                        ],
                        "Cron": [
                            {
                                "Days": [
                                    1
                                ],
                                "WDays": [
                                    1
                                ],
                                "StartTime": "1231312414",
                                "EndTime": "12313124111"
                            }
                        ],
                        "TimeTZone": "utc+8"
                    },
                    "ExpireTime": 1
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "req-id-13123"
    }
}
```

