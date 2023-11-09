**Example 1: 获取填写控件内容**

1.两个签署方只有其中一个已经填写, 另一个还没有填写
2. 发起方没有填写控件

Input: 

```
tccli essbasic ChannelDescribeFlowComponents --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowId yDSLZUUckpotjxzmUuyfZGu1pDwX4bPk
```

Output: 
```
{
    "Response": {
        "RecipientComponentInfos": [
            {
                "RecipientId": "yDSLZUUckpotjx66UuyfZGuByf4WemVW",
                "RecipientFillStatus": "1",
                "IsPromoter": true,
                "Components": []
            },
            {
                "RecipientId": "yDSLZUUckpotjxcdUuyfZGu82RFFYdHE",
                "RecipientFillStatus": "0",
                "IsPromoter": false,
                "Components": [
                    {
                        "ComponentId": "ComponentId_16",
                        "ComponentName": "学历",
                        "ComponentFillStatus": "0",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_18",
                        "ComponentName": "省市区",
                        "ComponentFillStatus": "0",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_15",
                        "ComponentName": "地址",
                        "ComponentFillStatus": "0",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_7",
                        "ComponentName": "单行文本",
                        "ComponentFillStatus": "0",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_8",
                        "ComponentName": "多行文本",
                        "ComponentFillStatus": "0",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_9",
                        "ComponentName": "选择器",
                        "ComponentFillStatus": "0",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_10",
                        "ComponentName": "数字",
                        "ComponentFillStatus": "0",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    }
                ]
            },
            {
                "RecipientId": "yDSLZUUckpotjx6cUuyfZGuupzb9E3yE",
                "RecipientFillStatus": "1",
                "IsPromoter": false,
                "Components": [
                    {
                        "ComponentId": "ComponentId_17",
                        "ComponentName": "性别",
                        "ComponentFillStatus": "1",
                        "ComponentValue": "男",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_11",
                        "ComponentName": "日期",
                        "ComponentFillStatus": "1",
                        "ComponentValue": "2023年11月09日",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentId": "ComponentId_12",
                        "ComponentName": "图片",
                        "ComponentFillStatus": "1",
                        "ComponentValue": "yDSLZUUckpooulteUE6T6QdzKPBmwiri",
                        "ImageUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=ffe60eceb87e57f6d25a420ab707eb90daafe04c630d50a58a3c5c97272ab5d1e19c84aafda8d25743e42218f3c94a2c82f34c646673ae5be179f5ab79723d5b9bff81faccea997027bd7b67b97629f95e9832cf510e48ba44456d966eb5cff86885bce1334b852989b53c635bffb7dc"
                    },
                    {
                        "ComponentId": "ComponentId_14",
                        "ComponentName": "邮箱",
                        "ComponentFillStatus": "1",
                        "ComponentValue": "xishizhaohua@qq.com",
                        "ImageUrl": ""
                    }
                ]
            }
        ],
        "RequestId": "059b2b26-d318-4555-8dc0-0ab4d9749a94"
    }
}
```

