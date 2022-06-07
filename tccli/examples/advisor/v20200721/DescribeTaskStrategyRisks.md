**Example 1: 查询评估项风险实例列表**



Input: 

```
tccli advisor DescribeTaskStrategyRisks --cli-unfold-argument  \
    --StrategyId 9
```

Output: 
```
{
    "Response": {
        "RequestId": "111",
        "RiskFieldsDesc": [
            {
                "Field": "InstanceId",
                "FieldName": "ID",
                "FieldType": "string",
                "FieldDict": {}
            },
            {
                "Field": "InstanceName",
                "FieldName": "名称",
                "FieldType": "string",
                "FieldDict": {}
            },
            {
                "Field": "InstanceState",
                "FieldName": "状态",
                "FieldType": "string",
                "FieldDict": {}
            },
            {
                "Field": "Zone",
                "FieldName": "可用区",
                "FieldType": "string",
                "FieldDict": {}
            },
            {
                "Field": "PrivateIPAddresses",
                "FieldName": "IP地址(内)",
                "FieldType": "stringSlice",
                "FieldDict": {}
            },
            {
                "Field": "PublicIPAddresses",
                "FieldName": "IP地址(公)",
                "FieldType": "stringSlice",
                "FieldDict": {}
            },
            {
                "Field": "Region",
                "FieldName": "地域",
                "FieldType": "string",
                "FieldDict": {}
            },
            {
                "Field": "Tags",
                "FieldName": "标签",
                "FieldType": "tags",
                "FieldDict": {}
            }
        ],
        "RiskTotalCount": 3,
        "ResourceCount": 10,
        "Risks": "[{\"InstanceId\":\"ins-xxx1\",\"InstanceName\":\"xxx1\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.2\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"},{\"InstanceId\":\"ins-xxx2\",\"InstanceName\":\"xxx2\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.11\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"}]",
        "StrategyId": 9
    }
}
```

