**Example 1: 示例**

示例

Input: 

```
tccli cwp DescribeWebHookPolicy --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CustomFields": [
                    {
                        "Key": "机器a",
                        "Value": "文本"
                    }
                ],
                "Events": [
                    {
                        "ControlBit": "1010",
                        "Type": 18
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 17
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 2
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 6
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 9
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 10
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 11
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 15
                    },
                    {
                        "ControlBit": "1010",
                        "Type": 16
                    },
                    {
                        "ControlBit": "1",
                        "Type": 21
                    },
                    {
                        "ControlBit": "1",
                        "Type": 24
                    }
                ],
                "Format": 0,
                "HostCount": 3,
                "HostLabels": [
                    {
                        "Type": 4,
                        "Values": [
                            "Value1"
                        ]
                    }
                ],
                "Id": 38,
                "IsDisabled": 0,
                "Name": "机器人",
                "Quuids": [
                    "058e0cf8-ba52-47fc-a100-2fdcc1e73e96",
                    "00e800cb-7202-4d83-90c2-6e920758dd42",
                    "380add75-bb06-4cc4-84c5-cf806d102fba"
                ],
                "Receivers": [
                    {
                        "Addr": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d0c2fc25-23a2-4285-ab98-d8a**",
                        "Id": 17,
                        "Name": "企微"
                    }
                ]
            }
        ],
        "RequestId": "6933d139-3143-4590-805f-712489ea91b8",
        "TotalCount": 16
    }
}
```

