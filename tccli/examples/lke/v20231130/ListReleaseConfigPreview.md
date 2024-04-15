**Example 1: 获取待发布的配置项**

获取待发布的配置项

Input: 

```
tccli lke ListReleaseConfigPreview --cli-unfold-argument  \
    --BotBizId 1747951478630252544 \
    --PageNumber 1 \
    --PageSize 15
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Action": 2,
                "ConfigItem": "应用名称",
                "Content": "",
                "LastValue": "",
                "UpdateTime": "1709694760",
                "Value": "上博"
            },
            {
                "Action": 2,
                "ConfigItem": "头像",
                "Content": "应用图标变更",
                "LastValue": "",
                "UpdateTime": "1709694760",
                "Value": "https://cdn.xiaowei.qq.com/lke/assets//static/avatar.png"
            },
            {
                "Action": 2,
                "ConfigItem": "欢迎语",
                "Content": "",
                "LastValue": "",
                "UpdateTime": "1709694760",
                "Value": "您好，我是客服助手，我将为您提供友好、专业和高效的服务。"
            },
            {
                "Action": 2,
                "ConfigItem": "输出方式",
                "Content": "",
                "LastValue": "非流式输出",
                "UpdateTime": "1709694760",
                "Value": "流式输出"
            },
            {
                "Action": 2,
                "ConfigItem": "通用模型回复开关",
                "Content": "",
                "LastValue": "关闭",
                "UpdateTime": "1709694760",
                "Value": "开启"
            },
            {
                "Action": 2,
                "ConfigItem": "默认问题回复",
                "Content": "",
                "LastValue": "",
                "UpdateTime": "1709694760",
                "Value": "作为一个智能助手，针对您这个问题，我所提供的答案或建议可能会存在不准确的地方。建议您转到人工，由专业顾问为您提供服务。"
            },
            {
                "Action": 2,
                "ConfigItem": "问答最大召回数量",
                "Content": "",
                "LastValue": "0",
                "UpdateTime": "1709694760",
                "Value": "3"
            },
            {
                "Action": 2,
                "ConfigItem": "回复灵活度",
                "Content": "",
                "LastValue": "已采纳答案润色回复",
                "UpdateTime": "1709694760",
                "Value": "已采纳答案直接回复"
            },
            {
                "Action": 2,
                "ConfigItem": "知识来源问答配置",
                "Content": "",
                "LastValue": "关闭",
                "UpdateTime": "1709694760",
                "Value": "开启"
            },
            {
                "Action": 2,
                "ConfigItem": "知识来源任务流程配置",
                "Content": "",
                "LastValue": "关闭",
                "UpdateTime": "1709694760",
                "Value": "开启"
            },
            {
                "Action": 2,
                "ConfigItem": "文档最大召回数量",
                "Content": "",
                "LastValue": "0",
                "UpdateTime": "1709694760",
                "Value": "4"
            },
            {
                "Action": 2,
                "ConfigItem": "知识来源文档配置",
                "Content": "",
                "LastValue": "关闭",
                "UpdateTime": "1709694760",
                "Value": "开启"
            },
            {
                "Action": 2,
                "ConfigItem": "上下文指代轮次",
                "Content": "",
                "LastValue": "0",
                "UpdateTime": "1709694760",
                "Value": "1"
            }
        ],
        "RequestId": "ac6c9baf-890b-4b63-b1b3-409eb74b0e14",
        "Total": "13"
    }
}
```

