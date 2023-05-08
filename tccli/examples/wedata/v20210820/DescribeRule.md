**Example 1: 查询规则详情**



Input: 

```
tccli wedata DescribeRule --cli-unfold-argument  \
    --ProjectId 1 \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CompareRule": {
                "Items": [
                    {
                        "Operator": "xx",
                        "ValueComputeType": 1,
                        "ValueList": [
                            {
                                "ValueType": 1,
                                "Value": "xx"
                            }
                        ],
                        "CompareType": 1
                    }
                ]
            },
            "ConditionType": 1,
            "RuleTemplateContent": "xx",
            "Name": "xx",
            "RuleGroupId": 1,
            "SourceObjectDataType": 1,
            "RuleId": 1,
            "AlarmLevel": 1,
            "SourceObjectValue": "xx",
            "RuleTemplateId": 1,
            "SourceObjectDataTypeName": "xx",
            "TableId": 1,
            "CustomSql": "xx",
            "Operator": "xx",
            "Description": "xx",
            "Type": 1,
            "ConditionExpression": "xx",
            "SourceObjectType": 1,
            "QualityDim": 1
        },
        "RequestId": "xx"
    }
}
```

