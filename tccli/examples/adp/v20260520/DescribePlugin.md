**Example 1: 获取插件详情**



Input: 

```
tccli adp DescribePlugin --cli-unfold-argument  \
    --PluginId c813b306-e49a-46ac-9bb9-c6897df4de4d \
    --SpaceId default_space
```

Output: 
```
{
    "Response": {
        "Plugin": {
            "CreateTime": "1745313719",
            "Operation": {
                "AllowExternalAccess": false,
                "BillingType": 1,
                "CategoryKey": "productivity_tools",
                "Introduction": "插件描述：该接口支持对全网范围进行网页搜索。",
                "IsRecommended": false
            },
            "PluginId": "c813b306-e49a-46ac-9bb9-c6897df4de4d",
            "PluginVersion": 2,
            "Profile": {
                "Author": "智能体开发平台",
                "Description": "搜索引擎工具，支持对全网范围进行网页搜索",
                "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/%E5%AE%98%E6%96%B9%E6%8F%92%E4%BB%B64%E6%9C%8817%E5%8F%B7%202/%E6%90%9C%E7%8B%97%E6%90%9C%E7%B4%A2.png",
                "Name": "搜狗搜索",
                "PluginClass": 1,
                "PluginKind": 2,
                "PluginSource": 1
            },
            "Statistics": {
                "CallCount": 355,
                "ToolCount": 1
            },
            "Status": 1,
            "ToolList": [
                {
                    "Billing": {
                        "BillingType": 1
                    },
                    "CallCount": 355,
                    "Description": "搜狗搜索工具，支持对全网范围进行网页搜索。",
                    "Name": "SougouWebSearch",
                    "PluginId": "c813b306-e49a-46ac-9bb9-c6897df4de4d",
                    "ToolAccessMode": 0,
                    "ToolConfig": {
                        "MCPToolConfig": {
                            "Inputs": [
                                {
                                    "AnyOf": [],
                                    "DefaultValue": "",
                                    "Description": "指定网址搜索，仅支持单域名筛选，例如:zhihu.com",
                                    "IsGlobalHidden": false,
                                    "IsRequired": false,
                                    "Name": "Insite",
                                    "OneOf": [],
                                    "SubParams": [],
                                    "Type": 0
                                }
                            ],
                            "Outputs": [
                                {
                                    "Description": "",
                                    "Name": "result",
                                    "RenderMode": 0,
                                    "SubParams": [
                                        {
                                            "Description": "",
                                            "Name": "content",
                                            "RenderMode": 0,
                                            "SubParams": [
                                                {
                                                    "Description": "",
                                                    "Name": "type",
                                                    "RenderMode": 0,
                                                    "SubParams": [],
                                                    "Type": 0
                                                }
                                            ],
                                            "Type": 9
                                        }
                                    ],
                                    "Type": 4
                                }
                            ]
                        }
                    },
                    "ToolId": "1146f40c-d466-43f1-94a8-721b2b71e711"
                }
            ],
            "UpdateTime": "1780533001",
            "UserState": {
                "IsFavorite": false,
                "IsInWhiteList": false,
                "WhiteListType": 0
            }
        },
        "RequestId": "6b47ad2d-8c26-4859-8518-4e2837096e8e"
    }
}
```

