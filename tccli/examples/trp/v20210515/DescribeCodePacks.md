**Example 1: 查询码包列表**



Input: 

```
tccli trp DescribeCodePacks --cli-unfold-argument  \
    --Keyword 关键词 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "CodePacks": [
            {
                "PackId": "码包ID字符串",
                "CorpId": 10000,
                "MerchantId": "eqdmnz7020bmtvi9",
                "CreateTime": "2021-12-01T06:48:45.000Z",
                "UpdateTime": "2021-12-01T06:48:45.000Z",
                "Status": "done",
                "Log": "日志",
                "CreateUser": "10000",
                "Amount": 10,
                "CodeLength": 32,
                "CodeType": "0",
                "Cipher": 0,
                "TextUrl": "https://xxx.xxx.com/texturl",
                "PackUrl": "https://xxx.xxx.com/packurl",
                "MerchantName": "商户名称",
                "RuleType": 0,
                "CustomId": "自定义码规则ID",
                "PackType": 0,
                "PackLevel": 1,
                "PackSpec": [
                    {
                        "Level": 1,
                        "Rate": 1,
                        "Amount": 1,
                        "CustomId": "用户自定义规则ID",
                        "CodeParts": [
                            {
                                "Name": "名称",
                                "Type": "类型",
                                "Value": "具体的值",
                                "Length": 8,
                                "Ext": ""
                            }
                        ],
                        "Unit": "个",
                        "SceneCode": 0
                    }
                ],
                "ProductName": "abc",
                "ProductSpecification": "abc",
                "ProductId": "abc",
                "RelateType": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "14b0a199-42cc-405c-984a-b5bcffe5600"
    }
}
```

