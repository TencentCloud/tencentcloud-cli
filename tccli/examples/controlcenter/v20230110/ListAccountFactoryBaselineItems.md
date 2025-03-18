**Example 1: 示例**

控制台获取账号基线列表

Input: 

```
tccli controlcenter ListAccountFactoryBaselineItems --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BaselineItems": [
            {
                "Classify": "消息",
                "ClassifyEn": "Message",
                "DependsOn": [
                    {
                        "Identifier": "TCC-AF_ACCOUNT_CONTACT",
                        "Type": "AccountFactorySetUp"
                    }
                ],
                "Description": "可以为每类消息设置接收人。账户、产品、故障等重要消息，建议您务必设置接收，防止消息遗漏造成损失。",
                "DescriptionEn": "Specify recipients for the notifications of different products. To avoid unexpected losses, we recommend you subscribe to important messages related to accounts, products, and errors.",
                "Identifier": "TCC-AF_ACCOUNT_NOTIFICATION",
                "Name": "消息订阅",
                "NameEn": "Message subscriptions",
                "Required": 0,
                "Weight": 8
            }
        ],
        "RequestId": "885a87d0-af7d-414a-b128-fd13653387b7",
        "Total": 1
    }
}
```

