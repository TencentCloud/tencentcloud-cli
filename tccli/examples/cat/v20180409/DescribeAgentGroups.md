**Example 1: 查询拨测分组列表示例**



Input: 

```
tccli cat DescribeAgentGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SysDefaultGroup": {
            "GroupId": 100000003,
            "GroupName": "免费用户默认组",
            "IsDefault": 1,
            "MaxGroupNum": 5,
            "TaskNum": 1,
            "GroupDetail": [
                {
                    "Isp": "cuc",
                    "IspName": "联通",
                    "Province": "tj",
                    "ProvinceName": "天津"
                }
            ]
        },
        "CustomGroups": [
            {
                "GroupId": 100004182,
                "GroupName": "SelfTestAgentGroup",
                "TaskNum": 0,
                "IsDefault": 0,
                "MaxGroupNum": 5,
                "GroupDetail": [
                    {
                        "Isp": "cmc",
                        "IspName": "移动",
                        "Province": "gd",
                        "ProvinceName": "广东"
                    }
                ]
            },
            {
                "GroupId": 100004183,
                "GroupName": "SelfTestAgentGroup",
                "TaskNum": 0,
                "IsDefault": 0,
                "MaxGroupNum": 5,
                "GroupDetail": [
                    {
                        "Isp": "cmc",
                        "IspName": "移动",
                        "Province": "gd",
                        "ProvinceName": "广东"
                    }
                ]
            },
            {
                "GroupId": 100004185,
                "GroupName": "TestModifyAgentGroup",
                "TaskNum": 1,
                "IsDefault": 0,
                "MaxGroupNum": 5,
                "GroupDetail": [
                    {
                        "Isp": "cmc",
                        "IspName": "移动",
                        "Province": "gd",
                        "ProvinceName": "广东"
                    }
                ]
            }
        ],
        "RequestId": "47fc298b-b466-4c38-97d0-ee42858f3de5"
    }
}
```

