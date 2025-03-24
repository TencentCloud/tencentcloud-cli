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
        "RequestId": "aa-bb-cc-dd",
        "RiskFieldsDesc": [
            {
                "Field": "Level",
                "FieldName": "风险等级",
                "FieldType": "string",
                "FieldDict": [
                    {
                        "Key": "3",
                        "Value": "高风险"
                    },
                    {
                        "Key": "2",
                        "Value": "中风险"
                    }
                ]
            },
            {
                "Field": "AppId",
                "FieldName": "appid",
                "FieldType": "int",
                "FieldDict": null
            },
            {
                "Field": "RiskDays",
                "FieldName": "风险持续天数",
                "FieldType": "int",
                "FieldDict": null
            },
            {
                "Field": "conditionID",
                "FieldName": "条件ID",
                "FieldType": "int",
                "FieldDict": null
            }
        ],
        "RiskTotalCount": 3,
        "ResourceCount": 10,
        "Risks": "[{\"InstanceId\":\"ins-xxx1\",\"InstanceName\":\"xxx1\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.2\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"},{\"InstanceId\":\"ins-xxx2\",\"InstanceName\":\"xxx2\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.11\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"}]",
        "StrategyId": 9
    }
}
```

