**Example 1: 查询新企业安全组规则**

查询新企业安全组规则

Input: 

```
tccli cfw DescribeEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --Enable xx \
    --Protocol xx \
    --Description xx \
    --PageNo xx \
    --SourceContent xx \
    --ServiceTemplateId xx \
    --PageSize xx \
    --DestContent xx \
    --RuleAction xx \
    --Port xx
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "OrderIndex": "xx",
                "Protocol": "xx",
                "SourceType": "xx",
                "SourceContent": "xx",
                "DestType": "xx",
                "ServiceTemplateId": "xx",
                "DestContent": "xx",
                "RuleAction": "xx",
                "Port": "xx",
                "Description": "xx"
            }
        ],
        "TotalCount": "xx",
        "PageSize": "xx",
        "PageNo": "xx",
        "RequestId": "xx"
    }
}
```

