**Example 1: 查询VPC 规则列表**



Input: 

```
tccli fwm DescribeVpcAclRules --cli-unfold-argument  \
    --GroupId fwmrg-yltolsxma7 \
    --Filters.0.Name RuleId \
    --Filters.0.Values 2ceddffe \
    --Filters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "AllTotalCount": 3,
        "RequestId": "f7d0cafa-6f06-49f5-862f-bf68897a762f",
        "Rules": [
            {
                "CreateTime": "2026-04-13 20:34:47",
                "Description": "1212",
                "DestContent": "::/0",
                "DestType": "net",
                "DnsParseCnt": 0,
                "EdgeId": "ALL",
                "FwGroupId": "ALL",
                "IpVersion": "ipv6",
                "ParamTemplateId": "",
                "Port": "-1/-1",
                "Protocol": "ANY",
                "RuleAction": "accept",
                "RuleId": "2ceddffe-a328-4bdf-af5f-a02821fab173",
                "Sequence": 3,
                "SourceContent": "::/0",
                "SourceType": "net",
                "UpdateTime": "2026-04-15 11:05:06"
            }
        ],
        "TotalCount": 1
    }
}
```

