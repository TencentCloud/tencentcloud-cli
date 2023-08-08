**Example 1: 查询流程填写控件**

查询流程填写控件

Input: 

```
tccli ess DescribeFlowComponents --cli-unfold-argument  \
    --Operator.UserId yDwfGUUcxxxxxxxxxxxxxxxxxxxx7mox \
    --FlowId yDwgNUUcxxxxxxxxxxxxxxxCs8eRqmy
```

Output: 
```
{
    "Response": {
        "RecipientComponentInfos": [
            {
                "Components": [
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_13",
                        "ComponentName": "多行文本",
                        "ComponentValue": "222",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_12",
                        "ComponentName": "单行文本",
                        "ComponentValue": "111",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_14",
                        "ComponentName": "勾选框",
                        "ComponentValue": "true",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_16",
                        "ComponentName": "数字",
                        "ComponentValue": "1",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_15",
                        "ComponentName": "选择器",
                        "ComponentValue": "选项1",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_17",
                        "ComponentName": "图片",
                        "ComponentValue": "yDwgNUxxxxxxxxxxxxxxxxxxQp4Pz3qpQ",
                        "ImageUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PNG?hkey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj"
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_19",
                        "ComponentName": "日期",
                        "ComponentValue": "2023年06月15日",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_20",
                        "ComponentName": "地址",
                        "ComponentValue": "1122",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_21",
                        "ComponentName": "邮箱",
                        "ComponentValue": "ddd@qq.com",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_22",
                        "ComponentName": "学历",
                        "ComponentValue": "小学",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_23",
                        "ComponentName": "性别",
                        "ComponentValue": "男",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_24",
                        "ComponentName": "省市区",
                        "ComponentValue": "内蒙古xxxxxxxxxxxxxxxxxxxx",
                        "ComponentRecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj",
                        "ImageUrl": ""
                    }
                ],
                "IsPromoter": true,
                "RecipientFillStatus": "1",
                "RecipientId": "yDRCLUxxxxxxxxxxxxxxxg0vjoimj"
            },
            {
                "Components": [],
                "IsPromoter": false,
                "RecipientFillStatus": "",
                "RecipientId": "yDwgNUUcxxxxxxxxxxxxxxxxxxxxxxxx"
            },
            {
                "Components": [],
                "IsPromoter": false,
                "RecipientFillStatus": "",
                "RecipientId": "yDwgNUUckp1q9xxxxxxxxxxxxxxxxxxxxxxxx"
            }
        ],
        "RequestId": "3764a5de-xxxxxxxx-xxxxxxxx-bf3c-fab89f1cd1a1"
    }
}
```

