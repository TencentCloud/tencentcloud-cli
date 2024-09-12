**Example 1: 查询流程填写控件**

1.查询流程填写控件
2.流程参与方yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj所有的控件都填写完成
3.流程参与方yDxZzUyKQDKuigUuO4zjEC4rpqaa8QgB、yDxZzUyKQDKuihUuO4zjEy09jfapyHjn没有填写控件

Input: 

```
tccli ess DescribeFlowComponents --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
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
                        "ComponentValue": "转让期限：自2023年9月21日起至2025年9月30日",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_12",
                        "ComponentName": "单行文本",
                        "ComponentValue": "伍仟元整",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_14",
                        "ComponentName": "勾选框",
                        "ComponentValue": "true",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_16",
                        "ComponentName": "数字",
                        "ComponentValue": "5000",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_15",
                        "ComponentName": "选择器",
                        "ComponentValue": "选项1",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_17",
                        "ComponentName": "图片",
                        "ComponentValue": "yDRSRUUgygj6qnwfUuO4zjEwc193c2hH",
                        "ImageUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/yDRSRUUgygj6qnwfUuO4zjEwc193c2hH/0.PNG?hkey=a45a3e727c637df7826f9",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj"
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_19",
                        "ComponentName": "日期",
                        "ComponentValue": "2023年06月15日",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_20",
                        "ComponentName": "地址",
                        "ComponentValue": "广东省深圳市南山区海天二路33号",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_21",
                        "ComponentName": "邮箱",
                        "ComponentValue": "himer@xisi.com",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_22",
                        "ComponentName": "学历",
                        "ComponentValue": "小学",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_23",
                        "ComponentName": "性别",
                        "ComponentValue": "男",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_24",
                        "ComponentName": "省市区",
                        "ComponentValue": "广东省",
                        "ComponentRecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj",
                        "ImageUrl": ""
                    }
                ],
                "IsPromoter": true,
                "RecipientFillStatus": "1",
                "RecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpmj"
            },
            {
                "Components": [],
                "IsPromoter": false,
                "RecipientFillStatus": "",
                "RecipientId": "yDxZzUyKQDKuigUuO4zjEC4rpqaa8QgB"
            },
            {
                "Components": [],
                "IsPromoter": false,
                "RecipientFillStatus": "",
                "RecipientId": "yDxZzUyKQDKuihUuO4zjEy09jfapyHjn"
            }
        ],
        "RequestId": "d245a68d-e13b-xxxx-xxxx-e5adc794db24"
    }
}
```

