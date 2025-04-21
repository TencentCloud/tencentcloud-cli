**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAdminMenu --cli-unfold-argument  \
    --Os 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ModuleId": "010000000000",
                    "ModuleName": "监控中心",
                    "ModuleType": "menu",
                    "Oss": [
                        0,
                        2,
                        4,
                        5
                    ],
                    "ParentIds": [
                        "0"
                    ],
                    "Path": "/home",
                    "Purchased": 2,
                    "SupportOs": [
                        0,
                        2,
                        4,
                        5,
                        5
                    ]
                },
                {
                    "ModuleId": "010100000000",
                    "ModuleName": "全局总览",
                    "ModuleType": "menu",
                    "Oss": [
                        0,
                        2,
                        4,
                        5
                    ],
                    "ParentIds": [
                        "0",
                        "010000000000"
                    ],
                    "Path": "/home/overview",
                    "Purchased": 2,
                    "SupportOs": [
                        0,
                        2,
                        4,
                        5
                    ]
                }
            ]
        },
        "RequestId": "9431f5f5-8153-480a-ba87-eacae962fd81"
    }
}
```

