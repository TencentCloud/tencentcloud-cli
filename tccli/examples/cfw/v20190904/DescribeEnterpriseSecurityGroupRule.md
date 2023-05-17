**Example 1: 查询新企业安全组规则**

查询新企业安全组规则

Input: 

```
tccli cfw DescribeEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --SourceContent abc \
    --DestContent abc \
    --Description abc \
    --RuleAction abc \
    --Enable abc \
    --Port abc \
    --Protocol abc \
    --ServiceTemplateId abc \
    --PageNo abc \
    --PageSize abc \
    --RuleUuid 0
```

Output: 
```
{
    "Response": {
        "PageNo": "abc",
        "PageSize": "abc",
        "Rules": [
            {
                "SourceContent": "abc",
                "SourceType": "abc",
                "DestContent": "abc",
                "DestType": "abc",
                "Protocol": "abc",
                "Port": "abc",
                "ServiceTemplateId": "abc",
                "RuleAction": "abc",
                "Description": "abc",
                "OrderIndex": "abc",
                "Id": "abc",
                "Enable": "abc"
            }
        ],
        "TotalCount": "abc",
        "RequestId": "abc"
    }
}
```

