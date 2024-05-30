**Example 1: 查询标识列表**



Input: 

```
tccli trp DescribeTraceCodes --cli-unfold-argument  \
    --Keyword xfetmgoiky2nms6nk8 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "TraceCodes": [
            {
                "Code": "abc",
                "CorpId": 1,
                "PackId": "abc",
                "BatchId": "abc",
                "MerchantId": "abc",
                "ProductId": "abc",
                "Status": 1,
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "MerchantName": "abc",
                "ProductName": "abc",
                "AgentId": 1,
                "Level": 1,
                "PackSpec": [
                    {
                        "Level": 1,
                        "Rate": 1,
                        "Amount": 1,
                        "CustomId": "abc",
                        "CodeParts": [
                            {
                                "Name": "abc",
                                "Type": "abc",
                                "Value": "abc",
                                "Length": 1,
                                "Ext": "abc"
                            }
                        ],
                        "Unit": "abc",
                        "SceneCode": 0
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

