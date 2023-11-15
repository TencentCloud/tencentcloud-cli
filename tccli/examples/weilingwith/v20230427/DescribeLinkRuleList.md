**Example 1: 联动规则列表**

成功响应

Input: 

```
tccli weilingwith DescribeLinkRuleList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --TriggerType timer \
    --PageNumber 1 \
    --PageSize 1 \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "aa1ac6c0-5721-4a84-bf87-dbd285bac6b7",
        "Result": {
            "LinkRuleSet": [
                {
                    "ActionSet": [
                        {
                            "Id": 59,
                            "Name": "体验123"
                        },
                        {
                            "Id": 28,
                            "Name": "瞿杨动作"
                        }
                    ],
                    "BeginDate": "2023-05-03",
                    "EndDate": "2023-05-22",
                    "EventSet": [
                        {
                            "Id": 34,
                            "Name": "联动新增事件"
                        },
                        {
                            "Id": 33,
                            "Name": "体验"
                        }
                    ],
                    "Id": 24,
                    "Name": "体验",
                    "Status": 24,
                    "ValidPeriod": ""
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalPage": 7,
            "TotalRow": 7
        }
    }
}
```

