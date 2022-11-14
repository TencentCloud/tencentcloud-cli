**Example 1: 分页查询质量规则**



Input: 

```
tccli wedata DescribeRulesByPage --cli-unfold-argument  \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx \
    --PageNumber 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageSize 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
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
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

