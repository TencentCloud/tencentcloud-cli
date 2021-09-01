**Example 1: 查询机器人对话流**



Input: 

```
tccli cr DescribeBotFlow --cli-unfold-argument  \
    --Module AiApi \
    --Operation GetFlow
```

Output: 
```
{
    "Response": {
        "BotFlowList": [
            {
                "BotFlowId": "1",
                "BotFlowName": "2",
                "PhonePoolList": [
                    {
                        "PoolId": "8",
                        "PoolName": "9"
                    }
                ]
            }
        ],
        "RequestId": "12345-6789-test-from-rest4api",
        "SmsSignList": [
            {
                "SignId": "3",
                "SignName": "4"
            }
        ],
        "SmsTemplateList": [
            {
                "TemplateId": "5",
                "TemplateName": "6"
            }
        ]
    }
}
```

