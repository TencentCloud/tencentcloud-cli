**Example 1: 查询数据列表**



Input: 

```
tccli dlc DescribeDataMaskStrategies --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "14ba6c26-2d36-4646-b1c4-6fe8dc2711d5",
        "Strategies": [
            {
                "StrategyId": "9facbbd7-ab31-4f56-8657-f981f3fea223",
                "UserAppId": "1305424723",
                "Uin": "100018379117",
                "SubAccountUin": "100041604908",
                "StrategyName": "default_mask_1",
                "StrategyType": "",
                "StrategyDesc": "",
                "Groups": [
                    {
                        "WorkGroupId": 225289,
                        "StrategyType": "MASK_SHOW_FIRST_4"
                    }
                ],
                "Users": "",
                "State": 1,
                "CreateTime": 1753416120334,
                "UpdateTime": 1753416120334
            },
            {
                "StrategyId": "af088222-22f0-4e7b-a179-8640b4f29ac9",
                "UserAppId": "1305424723",
                "Uin": "100018379117",
                "SubAccountUin": "100018370021",
                "StrategyName": "default_mask_2",
                "StrategyType": "",
                "StrategyDesc": "",
                "Groups": [
                    {
                        "WorkGroupId": 225285,
                        "StrategyType": "MASK"
                    },
                    {
                        "WorkGroupId": 225284,
                        "StrategyType": "MASK_NONE"
                    }
                ],
                "Users": "",
                "State": 1,
                "CreateTime": 1752579358146,
                "UpdateTime": 1752579472439
            },
            {
                "StrategyId": "1f14426d-fb9c-4e91-98a9-41d9691d0186",
                "UserAppId": "1305424723",
                "Uin": "100018379117",
                "SubAccountUin": "100042020000",
                "StrategyName": "default_mask_3",
                "StrategyType": "",
                "StrategyDesc": "",
                "Groups": [
                    {
                        "WorkGroupId": 225284,
                        "StrategyType": "MASK_SHOW_FIRST_4"
                    },
                    {
                        "WorkGroupId": 225285,
                        "StrategyType": "MASK_SHOW_LAST_4"
                    }
                ],
                "Users": "",
                "State": 1,
                "CreateTime": 1752578536032,
                "UpdateTime": 1752578536032
            },
            {
                "StrategyId": "f4ac2013-d004-4b6a-b3f9-89dc313e8f44",
                "UserAppId": "1305424723",
                "Uin": "100018379117",
                "SubAccountUin": "100042020000",
                "StrategyName": "data_mask_4",
                "StrategyType": "",
                "StrategyDesc": "",
                "Groups": [
                    {
                        "WorkGroupId": 221485,
                        "StrategyType": "MASK_DATE_SHOW_YEAR"
                    }
                ],
                "Users": "",
                "State": 1,
                "CreateTime": 1752570666841,
                "UpdateTime": 1752570666841
            },
            {
                "StrategyId": "f9c49afd-d5f5-4a22-b4a5-80d66061601c",
                "UserAppId": "1305424723",
                "Uin": "100018379117",
                "SubAccountUin": "100040310000",
                "StrategyName": "default_mask_5",
                "StrategyType": "",
                "StrategyDesc": "",
                "Groups": [
                    {
                        "WorkGroupId": 225254,
                        "StrategyType": "MASK_NONE"
                    }
                ],
                "Users": "",
                "State": 1,
                "CreateTime": 1752213893224,
                "UpdateTime": 1752213893224
            },
            {
                "StrategyId": "7a5cc300-baad-44b8-a918-46883a8a8454",
                "UserAppId": "1305424723",
                "Uin": "100018379117",
                "SubAccountUin": "100018430000",
                "StrategyName": "default_mask_6",
                "StrategyType": "",
                "StrategyDesc": "",
                "Groups": [
                    {
                        "WorkGroupId": 225237,
                        "StrategyType": "MASK_NULL"
                    }
                ],
                "Users": "",
                "State": 1,
                "CreateTime": 1750851717526,
                "UpdateTime": 1750851717526
            },
            {
                "StrategyId": "72de85e2-887a-4a87-bf86-90fc90ff25fa",
                "UserAppId": "1305424723",
                "Uin": "100018379117",
                "SubAccountUin": "100018370000",
                "StrategyName": "default_mask_7",
                "StrategyType": "",
                "StrategyDesc": "",
                "Groups": [
                    {
                        "WorkGroupId": 225237,
                        "StrategyType": "MASK_SHOW_LAST_4"
                    }
                ],
                "Users": "",
                "State": 1,
                "CreateTime": 1750144801970,
                "UpdateTime": 1750257014072
            }
        ],
        "TotalCount": 7
    }
}
```

