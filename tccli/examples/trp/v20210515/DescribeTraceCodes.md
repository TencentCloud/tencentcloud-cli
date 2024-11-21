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
                "Code": "https://anxin.qq.com/q99j9ovp5c6sok7l5g",
                "CorpId": 10000,
                "PackId": "pn30msjjxdx",
                "BatchId": "20241022112952826",
                "MerchantId": "pn30msjjxwga",
                "ProductId": "97zu51y30awe",
                "Status": 1,
                "CreateTime": "2024-10-30T07:16:21.265Z",
                "UpdateTime": "2024-10-30T07:16:21.265Z",
                "MerchantName": "商家A",
                "ProductName": "产品A",
                "AgentId": 1,
                "Level": 1,
                "PackSpec": [
                    {
                        "Level": 1,
                        "Rate": 1,
                        "Amount": 100,
                        "CustomId": "97zu51y30ID1",
                        "CodeParts": [
                            {
                                "Name": "唯一标识",
                                "Type": "1",
                                "Value": "值A",
                                "Length": 5,
                                "Ext": ""
                            }
                        ],
                        "Unit": "单位A",
                        "SceneCode": 0
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

