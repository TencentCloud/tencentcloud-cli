**Example 1: 事件列表**

成功响应

Input: 

```
tccli weilingwith DescribeEventList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 1 \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "529a10d6-0f9d-4ff9-8989-5dd0dc12aef6",
        "Result": {
            "EventDetailSet": [
                {
                    "CreateTime": "2023-05-13 20:23:37",
                    "DeviceType": "",
                    "Id": 14,
                    "LinkRuleSet": [
                        {
                            "Id": 23,
                            "Name": ""
                        }
                    ],
                    "Name": "13",
                    "TriggerCondition": "x-json:",
                    "TriggerType": "timer",
                    "ValidPeriod": "",
                    "WID": ""
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalPage": 78,
            "TotalRow": 78
        }
    }
}
```

