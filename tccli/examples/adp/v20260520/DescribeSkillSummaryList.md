**Example 1: 查询skill列表**



Input: 

```
tccli adp DescribeSkillSummaryList --cli-unfold-argument  \
    --SpaceId default_space \
    --PageNumber 0 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "SkillSummaryList": [
            {
                "ClassificationInfo": {
                    "BillingType": 0,
                    "BuiltinSource": 1,
                    "CategoryKey": "adp_knowledge_engine",
                    "CreateType": 99,
                    "ProviderType": 1,
                    "SourceLink": ""
                },
                "CurrentVersionInfo": {
                    "AnalysisInfo": {
                        "AnalysisStatus": 2,
                        "RiskDescription": "",
                        "RiskLevel": 0,
                        "SecurityReportUrl": "https://tix.qq.com/search/skill?keyword=4a6b07d90c8335b2bf1e62e70d86170c"
                    },
                    "Version": "1.0.17",
                    "VersionId": "1c1f9828-bef0-4060-909a-06bb260119cc"
                },
                "IsFavorite": false,
                "Profile": {
                    "CreateTime": "1779183919",
                    "Creator": "智能体开发平台",
                    "Description": "管理 ADP 技能广场技能，重点支持 ADP 技能的搜索、查看详情、上架、更新，以及把搜索结果安装到本地目录。用户提出 ADP 技能广场、搜索技能、找技能、上架技能、发布技能、更新技能、查看技能详情、安装技能到本地、find skill、publish skill、update skill 等需求时使用。搜索时额外补充腾讯 Skillhub 结果；ADP 调用需要环境变量 ADPAPIKEY 和 ADPSPACEID。",
                    "DisplayDescription": "管理和发现技能。用户提出“你能帮我做 X 吗”“能不能做 X”“帮我做 X”“怎么做 X”“有没有工具/方法做 X”等任何想完成某项具体任务的请求时（例如语音识别、视频生成等），或提出需要创建技能、搜索技能、找某类技能、安装技能到本地、上架/发布/更新技能、查看技能详情时使用。创建技能时优先配合 skill-creator 完成创建、打包，并询问是否上架 ADP 技能广场（即“添加到自定义 skills”）",
                    "DisplayName": "ADP技能管理",
                    "IconUrl": "https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/public/adp/skill/skill_icon/skill_default.jpg",
                    "Name": "adp-skill-manager",
                    "UpdateTime": "1780458720"
                },
                "ShareList": [],
                "SkillId": "5dd39985-a496-4fef-b753-a9bdca1b8433"
            }
        ],
        "TotalCount": 84,
        "RequestId": "f9512cd3-fe81-4a11-a547-ef17996b195b"
    }
}
```

