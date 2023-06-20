**Example 1: 查询单元化规则列表**

查询单元化规则列表

Input: 

```
tccli tsf DescribeUnitRulesV2 --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-afsfas \
    --Offset 0 \
    --Limit 20 \
    --SearchWord xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "Content": [
                {
                    "Id": "abc",
                    "GatewayInstanceId": "abc",
                    "Name": "abc",
                    "Description": "abc",
                    "Status": "abc",
                    "UnitRuleItemList": [
                        {
                            "Id": "abc",
                            "UnitRuleId": "abc",
                            "Relationship": "abc",
                            "DestNamespaceId": "abc",
                            "DestNamespaceName": "abc",
                            "Name": "abc",
                            "Priority": 0,
                            "Description": "abc",
                            "UnitRuleTagList": [
                                {
                                    "UnitRuleItemId": "abc",
                                    "Id": "abc",
                                    "TagType": "abc",
                                    "TagField": "abc",
                                    "TagOperator": "abc",
                                    "TagValue": "abc"
                                }
                            ]
                        }
                    ],
                    "CreatedTime": "abc",
                    "UpdatedTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

