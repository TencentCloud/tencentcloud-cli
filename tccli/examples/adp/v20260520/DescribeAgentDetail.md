**Example 1: 获取Agent详情**



Input: 

```
tccli adp DescribeAgentDetail --cli-unfold-argument  \
    --AppId 20617**********9040 \
    --AgentId 722f****************************5f01
```

Output: 
```
{
    "Response": {
        "Agent": {
            "AdvancedConfig": {
                "MaxReasoningRound": 100
            },
            "AgentId": "722fafb7-37b6-4896-ba32-08617e605f01",
            "Instructions": "",
            "Model": {
                "Alias": "智谱GLM-5.1",
                "ContextWordsLimit": 0,
                "InstructionsWordsLimit": 20000,
                "ModelId": "TCADP/glm-5.1",
                "ModelParameters": {
                    "DeepThinking": "",
                    "MaxTokens": 16384,
                    "ReasoningEffort": "",
                    "ReplyFormat": "",
                    "StopSequenceList": [],
                    "Temperature": 1
                }
            },
            "PluginList": [
                {
                    "AuthConfigStatus": 2,
                    "Config": {
                        "AuthType": 0,
                        "EnableCamRoleAuth": false,
                        "HeaderParameterList": [],
                        "PluginId": "3ad93aae-587e-4bcc-ae07-ad13bfb1aaca",
                        "QueryParameterList": []
                    },
                    "Description": "从知识库中检索内容，并通过大模型润色回复",
                    "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E7%9F%A5%E8%AF%86%E5%BA%93%E9%97%AE%E7%AD%94.png",
                    "Name": "知识库问答",
                    "Status": 1
                }
            ],
            "SkillList": [
                {
                    "CurrentVersion": "1.0.0",
                    "Description": "Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.",
                    "DisplayDescription": "引导用户完成结构化的文档共同创作工作流程。当用户想要编写文档、提案、技术规范、决策文档或类似的结构化内容时使用。此工作流程可帮助用户高效传递上下文，通过迭代优化内容，并验证文档是否适合读者。当用户提及编写文档、创建提案、起草规范或执行类似文档任务时触发。",
                    "DisplayName": "文档共同创作",
                    "IconUrl": "",
                    "Name": "doc-coauthoring",
                    "SkillId": "ceb06595-9cc4-4ffb-a4c7-0413438265c4",
                    "SourceType": 3
                }
            ],
            "ToolList": [
                {
                    "Config": {
                        "Description": "大模型结合知识库内容回答用户问题",
                        "HeaderParameterList": [],
                        "InputList": [
                            {
                                "AnyOfList": [],
                                "Description": "用户的query",
                                "Input": {
                                    "InputType": 0
                                },
                                "IsHidden": false,
                                "IsRequired": true,
                                "Name": "Query",
                                "OneOfList": [],
                                "SubParameterList": [],
                                "Type": 0
                            }
                        ],
                        "IsDisabled": false,
                        "OutputList": [
                            {
                                "Description": "返回码。0正常，非0异常",
                                "Name": "Code",
                                "RenderMode": 0,
                                "SubParameterList": [],
                                "Type": 1
                            }
                        ],
                        "PluginId": "3ad93aae-587e-4bcc-ae07-ad13bfb1aaca",
                        "QueryParameterList": [],
                        "ToolId": "0ca8d482-1e77-462b-bc21-807c8f052f69",
                        "ToolSource": 0
                    },
                    "Name": "KnowledgeRetrievalAnswer",
                    "Status": 1,
                    "StreamMode": 1,
                    "ToolAccessMode": 0
                }
            ]
        },
        "RequestId": "20b8a7d2-a190-4b60-b48d-8f322ce2975b"
    }
}
```

