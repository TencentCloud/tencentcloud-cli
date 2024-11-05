**Example 1: 获取私有域列表**



Input: 

```
tccli privatedns DescribeForwardRuleList --cli-unfold-argument  \
    --Limit 200 \
    --Offset 0 \
    --Filters.0.Name RuleName \
    --Filters.0.Values 呵呵 \
    --Filters.1.Name RuleType \
    --Filters.1.Values DOWN \
    --Filters.2.Name ZoneId \
    --Filters.2.Values zone-04jlawty \
    --Filters.3.Name EndPointId \
    --Filters.3.Values eid-asdfadaf \
    --Filters.4.Name EndPointName \
    --Filters.4.Values zdjdhhh
```

Output: 
```
{
    "Response": {
        "RequestId": "8a4ea9cc-b1df-f8f8-ffe7efbe98f9ff85",
        "TotalCount": 5,
        "ForwardRuleSet": [
            {
                "Domain": "qq.com",
                "ZoneId": "zone-s8cs72d9",
                "RuleId": "fid-af2skm96n",
                "ForwardAddress": [
                    "1.1.1.1:53"
                ],
                "RuleType": "UP",
                "VpcSet": [
                    {
                        "Region": "ap-guangzhou",
                        "UniqVpcId": "vpc-dus89eks"
                    }
                ],
                "EndPointName": "终端节点1",
                "EndPointId": "eid-fxiuf872bsp",
                "RuleName": "转发规则名称",
                "UpdatedAt": "2022-09-09 10:45:44",
                "CreatedAt": "2022-09-09 10:45:44",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ]
            }
        ]
    }
}
```

