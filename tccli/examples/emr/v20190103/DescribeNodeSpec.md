**Example 1: 查询节点规格**



Input: 

```
tccli emr DescribeNodeSpec --cli-unfold-argument  \
    --ZoneId 190001 \
    --CvmPayMode 0 \
    --NodeType All \
    --TradeType 3 \
    --ProductId 30 \
    --SceneName Hadoop-Default
```

Output: 
```
{
    "Response": {
        "NodeSpecs": [
            {
                "CmnTypes": [],
                "NodeName": "Master 节点",
                "NodeType": "Master",
                "Types": [
                    {
                        "InstanceFamilies": [
                            {
                                "FamilyName": "标准型S6",
                                "InstanceFamily": "S6",
                                "InstanceTypes": [],
                                "Order": 60
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "bb613114-cbe0-4fc1-8845-1d69e4f35e7a"
    }
}
```

