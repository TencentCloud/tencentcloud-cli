**Example 1: DescribeSkillDetail**



Input: 

```
tccli adp DescribeSkillDetail --cli-unfold-argument  \
    --SkillId 9e488e0c-ee1f-4b1c-b745-0e0e6f97e8c3 \
    --SpaceId default_space \
    --VersionFilterList.0.Name Perspective \
    --VersionFilterList.0.ValueList USER
```

Output: 
```
{
    "Response": {
        "SkillDetail": {
            "ReferenceSummaryList": [],
            "SkillSummary": {
                "ClassificationInfo": {
                    "BillingType": 0,
                    "BuiltinSource": 0,
                    "CategoryKey": "",
                    "CreateType": 1,
                    "ProviderType": 3,
                    "SourceLink": ""
                },
                "CurrentVersionInfo": {
                    "AnalysisInfo": {
                        "AnalysisStatus": 2,
                        "RiskDescription": "",
                        "RiskLevel": 0,
                        "SecurityReportUrl": "https://tix.qq.com/search/skill?keyword=e8ef636d1c007ef8f26c7d291d5a1b57"
                    },
                    "Version": "1.0.5",
                    "VersionId": "9cc26b2f-e364-41e6-b7d0-26a8bc19b944",
                    "VersionStatus": 0
                },
                "IsFavorite": false,
                "NoticeList": [],
                "PermissionIdList": [
                    "adpSkillsCenterEdit"
                ],
                "Profile": {
                    "CreateTime": "1779071255",
                    "Creator": "channel@qq.com",
                    "Description": "Use this skill when the user asks for time, greeting, 时间, 问候, 打招呼, ping the greeting bot, 或显式提到 \"time-greeting\"。用途是返回一句带版本号、当前时间、时段问候语、固定签名句的问候消息，用来验证 skill 发布链路。",
                    "DisplayDescription": "1688 商品自动采集并上传到 OZON 平台",
                    "DisplayName": "time-greeting-update-高危",
                    "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/adp/skill/skill_icon/skill_default.jpg",
                    "Name": "time-greeting",
                    "UpdateTime": "1780902492"
                },
                "ShareList": [
                    {
                        "ApprovalId": "2058846163546755776",
                        "ShareSkillId": "9e488e0c-ee1f-4b1c-b745-0e0e6f97e8c3_shared",
                        "ShareVersion": "1.0.1",
                        "ShareVersionId": "274d8c10-85c0-41df-bbb5-8bfa93553a85",
                        "SkillId": "9e488e0c-ee1f-4b1c-b745-0e0e6f97e8c3",
                        "Status": 1
                    }
                ],
                "SkillId": "9e488e0c-ee1f-4b1c-b745-0e0e6f97e8c3",
                "SkillStatus": 3
            },
            "VersionList": [
                {
                    "AnalysisInfo": {
                        "AnalysisStatus": 2,
                        "RiskDescription": "",
                        "RiskLevel": 0,
                        "SecurityReportUrl": "https://tix.qq.com/search/skill?keyword=e8ef636d1c007ef8f26c7d291d5a1b57"
                    },
                    "Version": "1.0.5",
                    "VersionId": "9cc26b2f-e364-41e6-b7d0-26a8bc19b944",
                    "VersionStatus": 3
                }
            ]
        },
        "RequestId": "06102b66-8b7f-4e2f-92fd-548bf447e60c"
    }
}
```

