**Example 1: 样例**

样例

Input: 

```
tccli essbasic ChannelDescribeFlowComponents --cli-unfold-argument  \
    --Agent.AppId yDxxxxxxxxxxxxxxxxxxxxT8l \
    --Agent.ProxyOrganizationOpenId xxxxxxxx \
    --Agent.ProxyOperator.OpenId xxxxxxxx \
    --FlowId yDwxxxxxxxxxxxxxxxxxxxx1EZ
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
                        "ComponentId": "ComponentId_xxxxxx",
                        "ComponentName": "图片",
                        "ComponentValue": "yDxxxxxxxxxxxxxxxxxxxxxxxxxxx1Txm",
                        "ImageUrl": "https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx4cf5"
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_xx",
                        "ComponentName": "选择器",
                        "ComponentValue": "选择器123",
                        "ImageUrl": ""
                    },
                    {
                        "ComponentFillStatus": "1",
                        "ComponentId": "ComponentId_xx",
                        "ComponentName": "simpletext",
                        "ComponentValue": "simpletext123",
                        "ImageUrl": ""
                    }
                ],
                "IsPromoter": true,
                "RecipientFillStatus": "1",
                "RecipientId": "yDxxxxxxxxxxxxxxxxxxxzf2X"
            },
            {
                "Components": [
                    {
                        "ComponentFillStatus": "0",
                        "ComponentId": "ComponentId_xx",
                        "ComponentName": "企业全称",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    }
                ],
                "IsPromoter": false,
                "RecipientFillStatus": "0",
                "RecipientId": "yDxxxxxxxxxxxxxxxxxxxxxxxR3I2"
            },
            {
                "Components": [
                    {
                        "ComponentFillStatus": "0",
                        "ComponentId": "ComponentId_xx",
                        "ComponentName": "单行文本",
                        "ComponentValue": "",
                        "ImageUrl": ""
                    }
                ],
                "IsPromoter": false,
                "RecipientFillStatus": "0",
                "RecipientId": "yDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxY0"
            }
        ],
        "RequestId": "a34xxxxxxxxxxxxxxxxxxxxxxxxxxx6cf"
    }
}
```

