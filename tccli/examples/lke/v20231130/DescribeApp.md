**Example 1: DescribeApp**

获取企业下应用详情

Input: 

```
tccli lke DescribeApp --cli-unfold-argument  \
    --AppBizId 应用ID \
    --AppType knowledge_qa
```

Output: 
```
{
    "Response": {
        "AppBizId": "应用ID",
        "AppConfig": {
            "KnowledgeQa": {
                "Greeting": "欢迎语",
                "Model": {
                    "AliasName": "精调知识大模型高级版",
                    "ContextLimit": 0,
                    "Desc": "应用描述",
                    "HistoryLimit": 5,
                    "IsUseContext": true,
                    "Name": "cs-normal-70b",
                    "TokenBalance": 0,
                    "Temperature": "0.5",
                    "TopP": "0.5"
                },
                "Output": {
                    "BareAnswer": "保守回复语",
                    "Method": 1,
                    "QuestionClarifyKeywords": [],
                    "ShowQuestionClarify": false,
                    "UseGeneralKnowledge": true,
                    "UseQuestionClarify": false,
                    "UseRecommended": false
                },
                "Pattern": "standard",
                "Plugins": [
                    {
                        "Inputs": [
                            {
                                "DefaultValue": "",
                                "Desc": "用户的query",
                                "IsRequired": true,
                                "Name": "Query",
                                "SubParams": [],
                                "Type": 0
                            }
                        ],
                        "IsBindingKnowledge": true,
                        "PluginIcon": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/插件.png",
                        "PluginId": "3ad9ddae-587e-4bcc-ae07-ad13bfb1aaca",
                        "PluginName": "知识库问答",
                        "ToolDesc": "大模型结合知识库内容回答用户问题",
                        "ToolId": "0ca8d482-1e77-462b-bc21-xddd7c8f052f69",
                        "ToolName": "KnowledgeRetrievalAnswer"
                    }
                ],
                "RoleDescription": "角色描述",
                "Search": [
                    {
                        "Confidence": 0.7,
                        "DocTopN": 0,
                        "IsEnabled": true,
                        "QaTopN": 3,
                        "ReplyFlexibility": 1,
                        "ResourceStatus": 0,
                        "ShowSearchEngine": false,
                        "Type": "qa",
                        "UseSearchEngine": false
                    },
                    {
                        "Confidence": 0,
                        "DocTopN": 0,
                        "IsEnabled": false,
                        "QaTopN": 0,
                        "ReplyFlexibility": 0,
                        "ResourceStatus": 0,
                        "ShowSearchEngine": false,
                        "Type": "search",
                        "UseSearchEngine": false
                    },
                    {
                        "Confidence": 0.2,
                        "DocTopN": 5,
                        "IsEnabled": true,
                        "QaTopN": 0,
                        "ReplyFlexibility": 0,
                        "ResourceStatus": 0,
                        "ShowSearchEngine": false,
                        "Type": "doc",
                        "UseSearchEngine": false
                    },
                    {
                        "Confidence": 0,
                        "DocTopN": 0,
                        "IsEnabled": false,
                        "QaTopN": 0,
                        "ReplyFlexibility": 0,
                        "ResourceStatus": 0,
                        "ShowSearchEngine": false,
                        "Type": "taskflow",
                        "UseSearchEngine": false
                    }
                ],
                "SearchRange": {
                    "ApiVarAttrInfos": [
                        {
                            "ApiVarId": "自定义变量ID",
                            "AttrBizId": "标签ID"
                        }
                    ],
                    "Condition": "and"
                },
                "Workflow": {
                    "IsEnabled": true,
                    "UsePdl": false
                },
                "SearchStrategy": {
                    "StrategyType": 0,
                    "TableEnhancement": false
                },
                "SingleWorkflow": {
                    "IsEnable": false,
                    "Status": "单工作流状态",
                    "WorkflowDesc": "单工作流描述",
                    "WorkflowId": "单工作流ID",
                    "WorkflowName": "单工作流名称"
                },
                "ThoughtModel": {
                    "AliasName": "精调Function-call模型",
                    "ContextLimit": 0,
                    "Desc": "",
                    "HistoryLimit": 0,
                    "IsUseContext": false,
                    "Name": "function-call-pro",
                    "Temperature": "0.5",
                    "TokenBalance": 0,
                    "TopP": "0.5"
                }
            }
        },
        "AppKey": "应用秘钥",
        "AppStatus": 2,
        "AppStatusDesc": "运行中",
        "AppType": "knowledge_qa",
        "AppTypeDesc": "知识库问答",
        "AvatarInAppeal": false,
        "BareAnswerInAppeal": false,
        "BaseConfig": {
            "Avatar": "头像",
            "Desc": "",
            "Name": "我的智能应用"
        },
        "GreetingInAppeal": false,
        "NameInAppeal": false,
        "RequestId": "485126ca-468c-497b-ab96-b939a8e125bd",
        "RoleInAppeal": false
    }
}
```

