**Example 1: DescribeApp**

查询应用详情

Input: 

```
tccli adp DescribeApp --cli-unfold-argument  \
    --AppId 20**************184 \
    --Domain 1 \
    --FieldMask.Paths AppConfig \
    --StatusType 1
```

Output: 
```
{
    "Response": {
        "App": {
            "AuxiliaryInfo": {
                "Appeal": {
                    "AppealingStatus": {
                        "AvatarInAppeal": false,
                        "FallbackReplyInAppeal": false,
                        "GreetingInAppeal": false,
                        "NameInAppeal": false,
                        "RoleInAppeal": false
                    }
                },
                "SearchResourceStatus": {
                    "ResourceStatus": 1
                },
                "SpecialStatusInfo": {
                    "Status": 0
                },
                "SubStatus": {
                    "ApprovalId": "0",
                    "SubStatusList": []
                }
            },
            "Config": {
                "Experience": {
                    "Advanced": {
                        "EnableContextRewrite": true,
                        "EnableImageTextRetrieval": false,
                        "IntentAchievement": [
                            {
                                "Description": "问答回复",
                                "Name": "qa"
                            }
                        ],
                        "ReplyFlexibility": 1
                    },
                    "Conversation": {
                        "AiCall": {
                            "DigitalHuman": {
                                "AssetKey": "df************************ddadf0",
                                "Avatar": "https://virtualhuman-cos-prod-1251316161.cos.ap-nanjing.tencentcos.cn/wupload/xy/virtualhuman_crm_prod/website_buy/vnZ6ZZYY.png",
                                "Name": "艾朵_职业套装_站姿",
                                "PreviewUrl": "https://virtualhuman-cos-prod-1251316161.cos.ap-nanjing.tencentcos.cn/wupload/xy/virtualhuman_crm_prod/preview/vStr966G.png"
                            },
                            "EnableDigitalHuman": true,
                            "EnableVoiceCall": true,
                            "EnableVoiceInteract": true,
                            "Voice": {
                                "TimbreKey": "tts_female_55",
                                "VoiceName": "智小柔-聊天女声",
                                "VoiceType": 502001
                            }
                        },
                        "BackgroundImage": {
                            "Brightness": 117,
                            "LandscapeImageUrl": "https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/public/1744544193038090240/2060280711767285184/image/xdNgbZYwoJkwclZytKaa-2061707216749939200.jpg",
                            "OriginalImageUrl": "https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/public/1744544193038090240/2060280711767285184/image/xdNgbZYwoJkwclZytKaa-2061707216749939200.jpg",
                            "PortraitImageUrl": "https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/public/1744544193038090240/2060280711767285184/image/xdNgbZYwoJkwclZytKaa-2061707216749939200.jpg",
                            "ThemeColor": "#cc5631"
                        },
                        "EnableFallbackReply": true,
                        "EnableRecommended": true,
                        "EnableWebSearch": false,
                        "FallbackReply": "针对您这个问题，我暂时还无法进行回答，请换一个问题吧。",
                        "InputBoxConfig": {
                            "InputBoxButtons": [
                                1
                            ]
                        },
                        "Method": 1,
                        "RecommendPromptMode": 0
                    },
                    "Role": {
                        "RoleDescription": "我是提示词信息"
                    }
                },
                "Greeting": {
                    "Greeting": "你好欢迎语",
                    "OpeningQuestionList": [
                        "我的示例问题"
                    ]
                },
                "Memory": {
                    "Enabled": true,
                    "LongMemoryDay": 30,
                    "Model": {
                        "Alias": "DeepSeek-V3.2",
                        "HistoryLimit": 5,
                        "ModelId": "Deepseek/deepseek-v3.2",
                        "ModelParams": {
                            "DeepThinking": "",
                            "MaxTokens": 16384,
                            "ReasoningEffort": "",
                            "ReplyFormat": "",
                            "StopSequenceList": [],
                            "Temperature": 0.6,
                            "TopP": 0.6
                        }
                    },
                    "PromptContent": "",
                    "PromptMode": 0
                },
                "Mode": {},
                "Model": {
                    "AiOptimizeModel": {
                        "Model": {
                            "Alias": "youtu-mrc-standard",
                            "HistoryLimit": 0,
                            "ModelId": "Youtu/youtu-mrc-standard",
                            "ModelParams": {
                                "DeepThinking": "",
                                "MaxTokens": 4000,
                                "ReasoningEffort": "",
                                "ReplyFormat": "",
                                "StopSequenceList": [],
                                "Temperature": 0.7,
                                "TopP": 0.6
                            }
                        }
                    },
                    "FileParseModel": {
                        "Alias": "youtu-parsing-sync",
                        "Description": "",
                        "EnhancementMode": "",
                        "ModelId": "Youtu/youtu-parsing-sync",
                        "ModelProviderType": "",
                        "SupportedFileList": []
                    },
                    "GenerateModel": {
                        "Model": {
                            "Alias": "youtu-mrc-pro",
                            "HistoryLimit": 5,
                            "ModelId": "Youtu/youtu-mrc-pro",
                            "ModelParams": {
                                "DeepThinking": "",
                                "MaxTokens": 4000,
                                "ReasoningEffort": "",
                                "ReplyFormat": "",
                                "StopSequenceList": [],
                                "Temperature": 0.7,
                                "TopP": 0.6
                            }
                        }
                    },
                    "MultiModalQaModel": {
                        "Model": {
                            "Alias": "hunyuan-turbos-vision",
                            "HistoryLimit": 5,
                            "ModelId": "Hunyuan/hunyuan-turbos-vision",
                            "ModelParams": {
                                "DeepThinking": "",
                                "MaxTokens": 4096,
                                "ReasoningEffort": "",
                                "ReplyFormat": "",
                                "StopSequenceList": [],
                                "Temperature": 0.7,
                                "TopP": 0.6
                            }
                        }
                    },
                    "MultiModalUnderstandingModel": {
                        "Model": {
                            "Alias": "youtu-mllm",
                            "HistoryLimit": 5,
                            "ModelId": "Youtu/youtu-mllm",
                            "ModelParams": {
                                "DeepThinking": "",
                                "MaxTokens": 4000,
                                "ReasoningEffort": "",
                                "ReplyFormat": "",
                                "StopSequenceList": [],
                                "Temperature": 0.7,
                                "TopP": 0.6
                            }
                        }
                    },
                    "PromptRewriteModel": {
                        "Model": {
                            "Alias": "youtu-rewrite",
                            "HistoryLimit": 5,
                            "ModelId": "Youtu/youtu-rewrite",
                            "ModelParams": {
                                "DeepThinking": "",
                                "MaxTokens": 4000,
                                "ReasoningEffort": "",
                                "ReplyFormat": "",
                                "StopSequenceList": [],
                                "Temperature": 0.6,
                                "TopP": 0.9
                            }
                        }
                    },
                    "ThinkModel": {
                        "Model": {
                            "Alias": "youtu-intent-pro",
                            "HistoryLimit": 5,
                            "ModelId": "Youtu/youtu-intent-pro",
                            "ModelParams": {
                                "DeepThinking": "",
                                "MaxTokens": 4000,
                                "ReasoningEffort": "",
                                "ReplyFormat": "",
                                "StopSequenceList": [],
                                "Temperature": 0,
                                "TopP": 0.8
                            }
                        }
                    }
                },
                "WebSearch": {
                    "ApiKey": "",
                    "Enabled": false,
                    "Provider": "",
                    "TopN": 0
                },
                "Workflow": {
                    "EnablePDL": false
                }
            },
            "Metadata": {
                "AppId": "2060280711767285184",
                "AppMode": 1,
                "Avatar": "https://cdn.xiaowei.qq.com/static/adp/app-default-avatar.png",
                "CreateTime": "1780044175",
                "Description": "",
                "Name": "我的智能体应用03",
                "SpaceId": "default_space",
                "UpdateTime": "1780384282"
            },
            "SecretInfo": {
                "AppKey": "cwwjX**************************************************************************************c************************nptQWMSAtFeD",
                "CreateTime": "1780044174"
            },
            "ShareUrlInfo": {
                "AccessControl": {
                    "AccessType": 3,
                    "Enabled": true,
                    "Whitelist": [
                        {
                            "Type": 1,
                            "Values": [
                                "70000000"
                            ]
                        }
                    ]
                },
                "ShareUrl": "https://tde.xiaowei.cloud.tencent.com/webim_exp/#/chat/leSlPm"
            },
            "Status": {
                "Status": 2,
                "StatusDescription": "运行中"
            }
        },
        "RequestId": "ecb7efc6-5070-4c4b-818d-5110026d5cbe"
    }
}
```

