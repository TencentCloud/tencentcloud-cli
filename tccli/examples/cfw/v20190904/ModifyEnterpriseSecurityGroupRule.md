**Example 1: 修改单条企业安全组规则内容**

修改 RuleUuid 指定的企业安全组规则完整内容。

Input: 

```
tccli cfw ModifyEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RuleUuid 420001 \
    --ModifyType 0 \
    --Data.SourceContent 192.0.2.0/24 \
    --Data.SourceType net \
    --Data.DestContent 198.51.100.10 \
    --Data.DestType net \
    --Data.RuleAction accept \
    --Data.Description 允许文档网段访问HTTPS \
    --Data.OrderIndex 10 \
    --Data.Protocol TCP \
    --Data.Port 443 \
    --Data.ServiceTemplateId  \
    --Data.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "NewRuleUuid": 420001,
        "RequestId": "11111111-2222-4333-8444-555555555555"
    }
}
```

**Example 2: 关闭单条企业安全组规则**

关闭 RuleUuid 指定的企业安全组规则。

Input: 

```
tccli cfw ModifyEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RuleUuid 420002 \
    --ModifyType 1 \
    --Enable 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "NewRuleUuid": 420002,
        "RequestId": "22222222-3333-4444-8555-666666666666"
    }
}
```

**Example 3: 开启全部企业安全组规则**

开启全部企业安全组规则；RuleUuid 传 0。

Input: 

```
tccli cfw ModifyEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RuleUuid 0 \
    --ModifyType 2 \
    --Enable 1
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "NewRuleUuid": 0,
        "RequestId": "33333333-4444-4555-8666-777777777777"
    }
}
```

**Example 4: 将企业安全组规则修改为地域访问解析域名**

用户要求广州地域资产按 DNS 解析结果访问域名时，调用 DescribeCfwRules 和 DescribeEnterpriseSecurityGroupRule 获取原规则完整字段，调用 DescribeSecurityGroupRegionList 获取广州对应的 Region=ap-guangzhou，再完整提交修改。

Input: 

```
tccli cfw ModifyEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RuleUuid 420003 \
    --ModifyType 0 \
    --Data.SourceContent ap-guangzhou \
    --Data.SourceType region \
    --Data.DestContent example.org \
    --Data.DestType dnsparse \
    --Data.RuleAction log \
    --Data.Description 观察广州地域资产访问解析域名 \
    --Data.OrderIndex 12 \
    --Data.Protocol TCP \
    --Data.Port 443 \
    --Data.ServiceTemplateId  \
    --Data.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "NewRuleUuid": 420003,
        "RequestId": "44444444-5555-4666-8777-888888888888"
    }
}
```

