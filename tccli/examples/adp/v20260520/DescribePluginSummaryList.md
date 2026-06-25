**Example 1: 拉取插件列表**



Input: 

```
tccli adp DescribePluginSummaryList --cli-unfold-argument  \
    --SpaceId default_space
```

Output: 
```
{
    "Response": {
        "PluginList": [
            {
                "Operation": {
                    "AllowExternalAccess": false,
                    "BillingType": 2,
                    "CategoryKey": "image_processing",
                    "Introduction": "",
                    "IsRecommended": true
                },
                "PluginId": "adcda186-813b-4d70-bb3f-538a522fe4a5",
                "Profile": {
                    "Author": "智能体开发平台",
                    "Description": "腾讯混元生3D（Tencent HY 3D）基于自研生成式AI大模型，为开发者提供专业、高效的3D内容生成API服务。该接口支持文生3D、图生3D、八视图生3D等多种生成方式，几何结构精准，纹理细节丰富，模型还原度高，并具备智能拓扑优化、组件化生成、自动UV展开等高级处理能力。",
                    "IconUrl": "https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/public/adp/0d0b65f37d0651ef8c4dc61d7238617d_1780285068379.png",
                    "Name": "混元生3D AI3D",
                    "PluginClass": 0,
                    "PluginKind": 2,
                    "PluginSource": 1
                },
                "Statistics": {
                    "CallCount": 9,
                    "ToolCount": 4
                },
                "Status": 1,
                "UserState": {
                    "IsFavorite": false,
                    "IsInWhiteList": false,
                    "WhiteListType": 0
                }
            }
        ],
        "TotalCount": 787,
        "RequestId": "c3778060-c630-4243-80a3-58cd409898b4"
    }
}
```

