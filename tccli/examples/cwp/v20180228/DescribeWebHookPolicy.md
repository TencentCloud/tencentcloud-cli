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
                        "ControlBit": "11",
                        "Type": 4
                    },
                    {
                        "ControlBit": "11",
                        "Type": 13
                    },
                    {
                        "ControlBit": "1",
                        "Type": 14
                    },
                    {
                        "ControlBit": "",
                        "Type": 22
                    },
                    {
                        "ControlBit": "1",
                        "Type": 23
                    },
                    {
                        "ControlBit": "",
                        "Type": 1
                    },
                    {
                        "ControlBit": "11",
                        "Type": 3
                    },
                    {
                        "ControlBit": "1",
                        "Type": 7
                    },
                    {
                        "ControlBit": "1",
                        "Type": 12
                    },
                    {
                        "ControlBit": "1",
                        "Type": 19
                    },
                    {
                        "ControlBit": "1",
                        "Type": 20
                    },
                    {
                        "ControlBit": "",
                        "Type": 25
                    },
                    {
                        "ControlBit": "1",
                        "Type": 8
                    },
                    {
                        "ControlBit": "1111",
                        "Type": 18
                    },
                    {
                        "ControlBit": "1111",
                        "Type": 17
                    },
                    {
                        "ControlBit": "11111",
                        "Type": 2
                    },
                    {
                        "ControlBit": "111",
                        "Type": 6
                    },
                    {
                        "ControlBit": "1111",
                        "Type": 9
                    },
                    {
                        "ControlBit": "1111",
                        "Type": 10
                    },
                    {
                        "ControlBit": "1111",
                        "Type": 11
                    },
                    {
                        "ControlBit": "11",
                        "Type": 15
                    },
                    {
                        "ControlBit": "1111",
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
                        "Values": []
                    }
                ],
                "Id": 38,
                "IsDisabled": 0,
                "Name": "只有机器a；文本",
                "Quuids": [
                    "058e0cf8-ba52-47fc-a100-2fdcc1e73e96",
                    "00e800cb-7202-4d83-90c2-6e920758dd42",
                    "380add75-bb06-4cc4-84c5-cf806d102fba"
                ],
                "Receivers": [
                    {
                        "Addr": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d0c2fc25-23a2-4285-ab98-d8a862146a73",
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

