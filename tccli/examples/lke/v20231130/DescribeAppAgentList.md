**Example 1: 查询指定应用下的Agent列表**

查询指定应用下的Agent列表

Input: 

```
tccli lke DescribeAppAgentList --cli-unfold-argument  \
    --AppBizId 1906600044720291840
```

Output: 
```
{
    "Response": {
        "Agents": [
            {
                "AgentId": "mainagent-1906600044720291840",
                "HandoffDescription": "处理不了的事情都可以转交给我处理",
                "Handoffs": [],
                "IconUrl": "https://cdn.xiaowei.qq.com/static/lke/app-default-avatar.png",
                "Instructions": "# 任务目标\n扮演智能客服，向有特定要求的客户提供友好、简洁、智慧、客观且易于理解的回复。\n\n# 任务流程\n1. 接收客户的问题或需求。\n2. 使用简洁、智慧、客观且普通人可理解的语言来组织答案。\n3. 在准备回复前，对自己的回答进行再次审查和确认，以确保信息的准确性。\n4. 确保回复符合所有服务准则。\n5. 向客户提供回复。\n\n# 限制条件\n- 回答必须使用简洁、智慧、客观且普通人可理解的语言。\n- 回答前需进行审查和确认，确保信息准确无误。\n- 回答必须符合所有服务准则。\n- 不得直接回答用户问题，仅提供回复的组织和审查服务。",
                "IsStartingAgent": true,
                "Model": {
                    "HistoryLimit": 0,
                    "IsEnabled": true,
                    "ModelAliasName": "精调Function-call模型",
                    "ModelContextWordsLimit": "8K",
                    "ModelName": "function-call-pro",
                    "Temperature": 0.5,
                    "TopP": 0.5
                },
                "Name": "willzhen-test",
                "Plugins": [
                    {
                        "Headers": [],
                        "PluginId": "4dcbd619-670c-403d-9f3f-8284880e2ffa"
                    },
                    {
                        "Headers": [],
                        "PluginId": "36b35d23-a020-4e48-b641-58d7ad92fba7"
                    },
                    {
                        "Headers": [],
                        "PluginId": "751ec82b-dd2b-4969-8ca0-3db674d29b94"
                    },
                    {
                        "Headers": [],
                        "PluginId": "99898f10-42e0-4186-afcc-2a9ec85db95b"
                    }
                ],
                "Tools": [
                    {
                        "CreateType": 0,
                        "Headers": [],
                        "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E7%A7%91%E5%AD%A6%E8%AE%A1%E7%AE%97.png",
                        "Inputs": [
                            {
                                "AgentHidden": false,
                                "DefaultValue": "",
                                "Desc": "数学表达式，只能是数字或符号，示例: 2+2^5+8/3+66",
                                "IsRequired": true,
                                "Name": "Expression",
                                "SubParams": [],
                                "Type": 0
                            }
                        ],
                        "IsBindingKnowledge": false,
                        "McpServer": {
                            "Headers": [],
                            "McpServerUrl": "",
                            "SseReadTimeout": 0,
                            "Timeout": 0
                        },
                        "Outputs": [
                            {
                                "AgentHidden": false,
                                "Desc": "返回码。0正常，非0异常",
                                "Name": "Code",
                                "SubParams": [],
                                "Type": 1
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回信息。Code为0：success，Code非0: 异常信息",
                                "Name": "Msg",
                                "SubParams": [],
                                "Type": 0
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回数据。Code为0：CalculationResult，Code非0：{}",
                                "Name": "Data",
                                "SubParams": [
                                    {
                                        "AgentHidden": false,
                                        "Desc": "计算结果",
                                        "Name": "Result",
                                        "SubParams": [],
                                        "Type": 0
                                    }
                                ],
                                "Type": 4
                            }
                        ],
                        "PluginId": "4dcbd619-670c-403d-9f3f-8284880e2ffa",
                        "PluginName": "科学计算",
                        "PluginType": 1,
                        "Status": 0,
                        "ToolDesc": "科学计算",
                        "ToolId": "7624299e-490c-4ca6-8378-0fe432421491",
                        "ToolName": "Calculator"
                    },
                    {
                        "CreateType": 0,
                        "Headers": [],
                        "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E5%A4%A9%E6%B0%94.png",
                        "Inputs": [
                            {
                                "AgentHidden": false,
                                "DefaultValue": "",
                                "Desc": "地点，可以包含省、市、区县等",
                                "IsRequired": true,
                                "Name": "Location",
                                "SubParams": [],
                                "Type": 0
                            },
                            {
                                "AgentHidden": false,
                                "DefaultValue": "",
                                "Desc": "查询开始时间，格式为2006-01-02",
                                "IsRequired": false,
                                "Name": "StartTime",
                                "SubParams": [],
                                "Type": 0
                            },
                            {
                                "AgentHidden": false,
                                "DefaultValue": "",
                                "Desc": "查询结束时间，格式为2006-01-02",
                                "IsRequired": false,
                                "Name": "EndTime",
                                "SubParams": [],
                                "Type": 0
                            }
                        ],
                        "IsBindingKnowledge": false,
                        "McpServer": {
                            "Headers": [],
                            "McpServerUrl": "",
                            "SseReadTimeout": 0,
                            "Timeout": 0
                        },
                        "Outputs": [
                            {
                                "AgentHidden": false,
                                "Desc": "返回码。0正常，非0异常",
                                "Name": "Code",
                                "SubParams": [],
                                "Type": 1
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回信息。Code为0：success，Code非0: 异常信息",
                                "Name": "Msg",
                                "SubParams": [],
                                "Type": 0
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回数据。Code非0：{}，Code为0：WeatherContent",
                                "Name": "Data",
                                "SubParams": [
                                    {
                                        "AgentHidden": false,
                                        "Desc": "天级别的天气，WeatherInfo",
                                        "Name": "Results",
                                        "SubParams": [
                                            {
                                                "AgentHidden": false,
                                                "Desc": "日期，格式为2006-01-02",
                                                "Name": "Date",
                                                "SubParams": [],
                                                "Type": 0
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "天气",
                                                "Name": "Condition",
                                                "SubParams": [],
                                                "Type": 0
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "当前温度",
                                                "Name": "Temperature",
                                                "SubParams": [],
                                                "Type": 2
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "湿度",
                                                "Name": "Humidity",
                                                "SubParams": [],
                                                "Type": 2
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "空气质量",
                                                "Name": "AQI",
                                                "SubParams": [],
                                                "Type": 2
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "最高温度",
                                                "Name": "TemperatureHigh",
                                                "SubParams": [],
                                                "Type": 2
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "最低温度",
                                                "Name": "TemperatureLow",
                                                "SubParams": [],
                                                "Type": 2
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "当日天气情况",
                                                "Name": "WeatherDay",
                                                "SubParams": [],
                                                "Type": 0
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "风速",
                                                "Name": "WindSpeed",
                                                "SubParams": [],
                                                "Type": 2
                                            }
                                        ],
                                        "Type": 9
                                    }
                                ],
                                "Type": 4
                            }
                        ],
                        "PluginId": "36b35d23-a020-4e48-b641-58d7ad92fba7",
                        "PluginName": "天气",
                        "PluginType": 1,
                        "Status": 0,
                        "ToolDesc": "获取指定日期和地点的天气信息，只支持查询中国国内城市的天气",
                        "ToolId": "09721e75-4e28-4953-a771-e1bd0e5a5927",
                        "ToolName": "GetWeatherInfo"
                    },
                    {
                        "CreateType": 0,
                        "Headers": [],
                        "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E4%BB%A3%E7%A0%81%E8%A7%A3%E9%87%8A%E5%99%A8.png",
                        "Inputs": [
                            {
                                "AgentHidden": false,
                                "DefaultValue": "",
                                "Desc": "待执行的code",
                                "IsRequired": true,
                                "Name": "Code",
                                "SubParams": [],
                                "Type": 0
                            }
                        ],
                        "IsBindingKnowledge": false,
                        "McpServer": {
                            "Headers": [],
                            "McpServerUrl": "",
                            "SseReadTimeout": 0,
                            "Timeout": 0
                        },
                        "Outputs": [
                            {
                                "AgentHidden": false,
                                "Desc": "返回码。0正常，非0异常",
                                "Name": "Code",
                                "SubParams": [],
                                "Type": 1
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回信息。Code为0：success，Code非0: 异常信息",
                                "Name": "Msg",
                                "SubParams": [],
                                "Type": 0
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回数据。Code非0：{}，Code为0：CodeContent",
                                "Name": "Data",
                                "SubParams": [
                                    {
                                        "AgentHidden": false,
                                        "Desc": "代码执行结果",
                                        "Name": "ExecResult",
                                        "SubParams": [],
                                        "Type": 0
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "代码执行信息",
                                        "Name": "ExecMsg",
                                        "SubParams": [],
                                        "Type": 0
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "代码执行状态。success：成功，fail：失败",
                                        "Name": "ExecState",
                                        "SubParams": [],
                                        "Type": 0
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "处理后的图片列表",
                                        "Name": "Images",
                                        "SubParams": [
                                            {
                                                "AgentHidden": false,
                                                "Desc": "图片Url",
                                                "Name": "Url",
                                                "SubParams": [],
                                                "Type": 0
                                            }
                                        ],
                                        "Type": 9
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "处理后的文件列表",
                                        "Name": "Files",
                                        "SubParams": [
                                            {
                                                "AgentHidden": false,
                                                "Desc": "文件Url",
                                                "Name": "Url",
                                                "SubParams": [],
                                                "Type": 0
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "文件名称",
                                                "Name": "FileName",
                                                "SubParams": [],
                                                "Type": 0
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "文件大小",
                                                "Name": "Size",
                                                "SubParams": [],
                                                "Type": 1
                                            }
                                        ],
                                        "Type": 9
                                    }
                                ],
                                "Type": 4
                            }
                        ],
                        "PluginId": "751ec82b-dd2b-4969-8ca0-3db674d29b94",
                        "PluginName": "代码解释器",
                        "PluginType": 1,
                        "Status": 0,
                        "ToolDesc": "该工具用于代码执行",
                        "ToolId": "3af56855-015a-48d8-a6e0-b3ad0a6eddcb",
                        "ToolName": "CodeInterpreter"
                    },
                    {
                        "CreateType": 0,
                        "Headers": [],
                        "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E4%BB%A3%E7%A0%81%E8%A7%A3%E9%87%8A%E5%99%A8.png",
                        "Inputs": [
                            {
                                "AgentHidden": false,
                                "DefaultValue": "",
                                "Desc": "Python code that uses pyecharts to create visualization, the input code should be a valid python command. The code should create a chart and render it, then save it as a html file containing the interactive chart. Do not pip install missing modules.",
                                "IsRequired": true,
                                "Name": "Code",
                                "SubParams": [],
                                "Type": 0
                            }
                        ],
                        "IsBindingKnowledge": false,
                        "McpServer": {
                            "Headers": [],
                            "McpServerUrl": "",
                            "SseReadTimeout": 0,
                            "Timeout": 0
                        },
                        "Outputs": [
                            {
                                "AgentHidden": false,
                                "Desc": "返回码。0正常，非0异常",
                                "Name": "Code",
                                "SubParams": [],
                                "Type": 1
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回信息。Code为0：success，Code非0: 异常信息",
                                "Name": "Msg",
                                "SubParams": [],
                                "Type": 0
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回数据。Code非0：{}，Code为0：CodeContent",
                                "Name": "Data",
                                "SubParams": [
                                    {
                                        "AgentHidden": false,
                                        "Desc": "代码执行结果",
                                        "Name": "ExecResult",
                                        "SubParams": [],
                                        "Type": 0
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "代码执行信息",
                                        "Name": "ExecMsg",
                                        "SubParams": [],
                                        "Type": 0
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "代码执行状态。success：成功，fail：失败",
                                        "Name": "ExecState",
                                        "SubParams": [],
                                        "Type": 0
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "处理后的图片列表",
                                        "Name": "Images",
                                        "SubParams": [
                                            {
                                                "AgentHidden": false,
                                                "Desc": "图片Url",
                                                "Name": "Url",
                                                "SubParams": [],
                                                "Type": 0
                                            }
                                        ],
                                        "Type": 9
                                    },
                                    {
                                        "AgentHidden": false,
                                        "Desc": "处理后的文件列表",
                                        "Name": "Files",
                                        "SubParams": [
                                            {
                                                "AgentHidden": false,
                                                "Desc": "文件Url",
                                                "Name": "Url",
                                                "SubParams": [],
                                                "Type": 0
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "文件名称",
                                                "Name": "FileName",
                                                "SubParams": [],
                                                "Type": 0
                                            },
                                            {
                                                "AgentHidden": false,
                                                "Desc": "文件大小",
                                                "Name": "Size",
                                                "SubParams": [],
                                                "Type": 1
                                            }
                                        ],
                                        "Type": 9
                                    }
                                ],
                                "Type": 4
                            }
                        ],
                        "PluginId": "751ec82b-dd2b-4969-8ca0-3db674d29b94",
                        "PluginName": "代码解释器",
                        "PluginType": 1,
                        "Status": 0,
                        "ToolDesc": "适用于代码运行，并支持输出可交互式的图表",
                        "ToolId": "3ea907b0-0978-4f37-a771-7c53383c9a8e",
                        "ToolName": "GenerateCharts"
                    },
                    {
                        "CreateType": 0,
                        "Headers": [],
                        "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/03bigIcon%E5%A4%A7%E5%9B%BE%E6%A0%87%20%282%29.png",
                        "Inputs": [
                            {
                                "AgentHidden": false,
                                "DefaultValue": "",
                                "Desc": "对于图片的文字描述，算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。",
                                "IsRequired": true,
                                "Name": "Prompt",
                                "SubParams": [],
                                "Type": 0
                            }
                        ],
                        "IsBindingKnowledge": false,
                        "McpServer": {
                            "Headers": [],
                            "McpServerUrl": "",
                            "SseReadTimeout": 0,
                            "Timeout": 0
                        },
                        "Outputs": [
                            {
                                "AgentHidden": false,
                                "Desc": "返回码。0正常，非0异常",
                                "Name": "Code",
                                "SubParams": [],
                                "Type": 1
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回信息。Code为0：success，Code非0: 异常信息",
                                "Name": "Msg",
                                "SubParams": [],
                                "Type": 0
                            },
                            {
                                "AgentHidden": false,
                                "Desc": "返回数据。Code不为0：{}",
                                "Name": "Data",
                                "SubParams": [
                                    {
                                        "AgentHidden": false,
                                        "Desc": "",
                                        "Name": "Results",
                                        "SubParams": [
                                            {
                                                "AgentHidden": false,
                                                "Desc": "生成的图片URL",
                                                "Name": "Url",
                                                "SubParams": [],
                                                "Type": 0
                                            }
                                        ],
                                        "Type": 9
                                    }
                                ],
                                "Type": 4
                            }
                        ],
                        "PluginId": "99898f10-42e0-4186-afcc-2a9ec85db95b",
                        "PluginName": "图片生成",
                        "PluginType": 1,
                        "Status": 0,
                        "ToolDesc": "根据输入的文本描述，智能生成与之相关的结果图",
                        "ToolId": "da9264a2-a7ed-4095-b2fa-e94265e370dc",
                        "ToolName": "TextToImage"
                    }
                ],
                "WorkflowId": ""
            },
            {
                "AgentId": "50d09c49-0497-43e8-a380-8a673ea70c81",
                "HandoffDescription": "财务小助手",
                "Handoffs": [
                    "b07abb63-5c0b-4291-9eb6-b600d53bcc97",
                    "3333b8ad-1a78-4c4e-af6e-0c4beffb1631"
                ],
                "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png",
                "Instructions": "帮助我完成一些财务上的事情",
                "IsStartingAgent": true,
                "Model": {
                    "HistoryLimit": 4,
                    "IsEnabled": true,
                    "ModelAliasName": "精调Function-call模型",
                    "ModelContextWordsLimit": "8K",
                    "ModelName": "function-call-pro",
                    "Temperature": 0.5,
                    "TopP": 0.5
                },
                "Name": "财务小助手",
                "Plugins": [],
                "Tools": [],
                "WorkflowId": ""
            },
            {
                "AgentId": "db6fd2bb-c1ee-4173-8c94-327cd98f9293",
                "HandoffDescription": "当用户需要取消订单时触发此任务流程",
                "Handoffs": [],
                "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png",
                "Instructions": "{\"SLOTs\":\"- name: 订单id\\n  desc: 指的是订单id，10位阿拉伯数字，例如：1234567890。\\n  type: int\\n- name: 用户id\\n  desc: 指的是用户身份id，4位数阿拉伯数字，如：1234。\\n  type: int\\n\",\"APIs\":\"- name: 查询账户中是否有订单\\n  precondition: []\\n- name: 代码1\\n  precondition: []\\n- name: 判断是否已提交取消申请的SR工单\\n  precondition:\\n    - 查询账户中是否有订单\\n- name: 代码4\\n  precondition: []\\n- name: 查询订单状态\\n  precondition:\\n    - 判断是否已提交取消申请的SR工单\\n- name: 代码3\\n  precondition: []\\n- name: 识别SR单进度\\n  precondition:\\n    - 判断是否已提交取消申请的SR工单\\n- name: 代码2\\n  precondition: []\\n\",\"ANSWERs\":\"- name: 参数收集\\n  desc: 收集\\u003cSLOT\\u003e中定义的相关的参数. 若\\u003cconversation\\u003e中用户已经给出了参数值, 则跳过这一步; 否则, 以自然、连贯、亲切的方式询问用户.\\n- name: 工作流相关自由回复\\n  desc: 若用户当前的询问和工作流相关, 但不在当前工作流范围内, 请基于常识来回复用户的问题.\\n- name: 已通过\\n  desc: 您提交的取消订单申请，已通过。该订单已取消，取消后退款会1-3个工作日内原路返回。\\n- name: 未通过\\n  desc: 您好，经过客服的申请，您的该笔订单未通过取消申请，建议您正常入住。\\n- name: 处理中\\n  desc: 您好，您提交的取消订单申请正在处理中，客服会在30-60分钟内处理完成，处理完成后会通过短信或电话通知您，请您耐心等待。\\n- name: 未支付\\n  desc: 您好，您的订单还未支付，30分钟内未支付，该订单会自动取消。\\n- name: 已确认-可免费取消\\n  desc: 您好，您的订单已经确认，若您想取消的话，可点击下方按钮，直接取消。\\n- name: 已确定-有违约金\\n  desc: 您好，您的订单已经确定，酒店将为您整晚保留订单，不可免费取消。您取消的话，需要收取违约金\\\\*\\\\*\\\\*，建议您正常入住。\\n- name: 已取消\\n  desc: 您好，您的订单已取消，无需重复取消。\\n- name: 已入住\\n  desc: 您好，您的订单显示已经入住，无法直接取消呢，您可以点击下方【申请取消】按钮，客服收到您的取消申请，会第一时间帮您和酒店协商处理。感谢您的选择，祝您开心每一天。\\n- name: 已结账\\n  desc: 您好，您的订单显示已经完结，不可取消，请问还有什么可以帮您\\n- name: 客户不选择订单\\n  desc: 您好，如果您想咨询其他订单，也可以直接输入订单号，这边帮您处理\\n- name: 结束回复1\\n  desc: 抱歉，未查询到您账户下有订单，现在为您转接人工服务，请稍等\\n\"}",
                "IsStartingAgent": false,
                "Model": {
                    "HistoryLimit": 0,
                    "IsEnabled": false,
                    "ModelAliasName": "精调Function-call模型",
                    "ModelContextWordsLimit": "8K",
                    "ModelName": "function-call-pro",
                    "Temperature": 0.5,
                    "TopP": 0.5
                },
                "Name": "开发票",
                "Plugins": [],
                "Tools": [],
                "WorkflowId": "8c2cf597-c77f-46b3-b9be-16c62ef8f96a"
            },
            {
                "AgentId": "881bcd68-a93c-4715-96f0-f7aff3a025ca",
                "HandoffDescription": "当用户需要取消订单时触发此任务流程",
                "Handoffs": [],
                "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png",
                "Instructions": "{\"SLOTs\":\"- name: 订单id\\n  desc: 指的是订单id，10位阿拉伯数字，例如：1234567890。\\n  type: int\\n- name: 用户id\\n  desc: 指的是用户身份id，4位数阿拉伯数字，如：1234。\\n  type: int\\n\",\"APIs\":\"- name: 查询账户中是否有订单\\n  precondition: []\\n- name: 代码1\\n  precondition: []\\n- name: 判断是否已提交取消申请的SR工单\\n  precondition:\\n    - 查询账户中是否有订单\\n- name: 代码4\\n  precondition: []\\n- name: 查询订单状态\\n  precondition:\\n    - 判断是否已提交取消申请的SR工单\\n- name: 代码3\\n  precondition: []\\n- name: 识别SR单进度\\n  precondition:\\n    - 判断是否已提交取消申请的SR工单\\n- name: 代码2\\n  precondition: []\\n\",\"ANSWERs\":\"- name: 参数收集\\n  desc: 收集\\u003cSLOT\\u003e中定义的相关的参数. 若\\u003cconversation\\u003e中用户已经给出了参数值, 则跳过这一步; 否则, 以自然、连贯、亲切的方式询问用户.\\n- name: 工作流相关自由回复\\n  desc: 若用户当前的询问和工作流相关, 但不在当前工作流范围内, 请基于常识来回复用户的问题.\\n- name: 已通过\\n  desc: 您提交的取消订单申请，已通过。该订单已取消，取消后退款会1-3个工作日内原路返回。\\n- name: 未通过\\n  desc: 您好，经过客服的申请，您的该笔订单未通过取消申请，建议您正常入住。\\n- name: 处理中\\n  desc: 您好，您提交的取消订单申请正在处理中，客服会在30-60分钟内处理完成，处理完成后会通过短信或电话通知您，请您耐心等待。\\n- name: 未支付\\n  desc: 您好，您的订单还未支付，30分钟内未支付，该订单会自动取消。\\n- name: 已确认-可免费取消\\n  desc: 您好，您的订单已经确认，若您想取消的话，可点击下方按钮，直接取消。\\n- name: 已确定-有违约金\\n  desc: 您好，您的订单已经确定，酒店将为您整晚保留订单，不可免费取消。您取消的话，需要收取违约金\\\\*\\\\*\\\\*，建议您正常入住。\\n- name: 已取消\\n  desc: 您好，您的订单已取消，无需重复取消。\\n- name: 已入住\\n  desc: 您好，您的订单显示已经入住，无法直接取消呢，您可以点击下方【申请取消】按钮，客服收到您的取消申请，会第一时间帮您和酒店协商处理。感谢您的选择，祝您开心每一天。\\n- name: 已结账\\n  desc: 您好，您的订单显示已经完结，不可取消，请问还有什么可以帮您\\n- name: 客户不选择订单\\n  desc: 您好，如果您想咨询其他订单，也可以直接输入订单号，这边帮您处理\\n- name: 结束回复1\\n  desc: 抱歉，未查询到您账户下有订单，现在为您转接人工服务，请稍等\\n\"}",
                "IsStartingAgent": false,
                "Model": {
                    "HistoryLimit": 0,
                    "IsEnabled": false,
                    "ModelAliasName": "精调Function-call模型",
                    "ModelContextWordsLimit": "32K",
                    "ModelName": "function-call-pro",
                    "Temperature": 0.5,
                    "TopP": 0.5
                },
                "Name": "酒店取消预订",
                "Plugins": [],
                "Tools": [],
                "WorkflowId": "8c2cf597-c77f-46b3-b9be-16c62ef8f96a"
            },
            {
                "AgentId": "845c1ef7-5103-4e95-9e59-3d46fbeabe63",
                "HandoffDescription": "处理用户新闻搜索的需求",
                "Handoffs": [],
                "IconUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png",
                "Instructions": "根据用户的输入，搜索相关新闻，提供相应的web访问地址",
                "IsStartingAgent": false,
                "Model": {
                    "HistoryLimit": 5,
                    "IsEnabled": true,
                    "ModelAliasName": "精调Function-call模型",
                    "ModelContextWordsLimit": "32K",
                    "ModelName": "function-call-pro",
                    "Temperature": 0.5,
                    "TopP": 0.5
                },
                "Name": "新闻搜索agent",
                "Plugins": [],
                "Tools": [],
                "WorkflowId": ""
            }
        ],
        "RequestId": "0fe2c215-7e59-4f3d-a3c0-468d63c5d89e",
        "StaringAgentId": "mainagent-1906600044720291840"
    }
}
```

