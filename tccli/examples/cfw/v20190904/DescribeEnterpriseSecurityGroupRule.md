**Example 1: 查询新企业安全组规则**

查询新企业安全组规则

Input: 

```
tccli cfw DescribeEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --SourceContent 192.168.0.2 \
    --DestContent 192.168.0.3 \
    --Description 放行规则 \
    --RuleAction accept \
    --Enable true \
    --Port 80 \
    --Protocol TCP \
    --ServiceTemplateId ppmg-jz17vpis \
    --PageNo 1 \
    --PageSize 10 \
    --RuleUuid 1
```

Output: 
```
{
    "Response": {
        "PageNo": "1",
        "PageSize": "10",
        "Rules": [
            {
                "SourceContent": "192.168.0.2",
                "SourceType": "net",
                "DestContent": "192.168.0.3",
                "DestType": "net",
                "Protocol": "TCP",
                "Port": "80",
                "ServiceTemplateId": "ppmg-jz17vpis",
                "RuleAction": "accept",
                "Description": "放行规则",
                "OrderIndex": "1",
                "Id": "1",
                "Enable": "true"
            }
        ],
        "TotalCount": "1",
        "RequestId": "8f563b4d-8151-4db0-a822-9bde279d2079"
    }
}
```

