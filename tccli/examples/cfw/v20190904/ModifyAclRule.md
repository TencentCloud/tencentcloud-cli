**Example 1: 先查后完整修改一条互联网边界规则**

修改 Uuid 指定规则的 Description；其它可写字段随完整规则一并提交。

Input: 

```
tccli cfw ModifyAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.10 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.20 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction accept \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 3 \
    --Rules.0.Uuid 246810 \
    --Rules.0.Enable true \
    --Rules.0.Description 允许文档示例业务访问 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0 \
    --Rules.0.LogId alert-log-example-001 \
    --Rules.0.ParamTemplateId 
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            246810
        ],
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

**Example 2: 按用户要求将规则修改为观察广东来源入站访问**

用户要求“将规则修改为观察广东来源的入站访问”时，先调用 DescribeAclRegInfo，按规则 Scope=serial 传 FwType=["SERIAL"]，从 Data 中精确匹配 RegionName=广东省并取得 RegionCode=gd44；再调用 DescribeCfwRules 查询目标规则，完整携带原规则可写字段，并把入站来源改为 location 和 gd44。

Input: 

```
tccli cfw ModifyAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent gd44 \
    --Rules.0.SourceType location \
    --Rules.0.TargetContent 198.51.100.20 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex 4 \
    --Rules.0.Uuid 246811 \
    --Rules.0.Enable true \
    --Rules.0.Description 观察广东来源入站访问 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0 \
    --Rules.0.LogId  \
    --Rules.0.ParamTemplateId 
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            246811
        ],
        "RequestId": "00000000-0000-4000-8000-000000000003"
    }
}
```

**Example 3: 将互联网边界规则修改为域名规则**

先查询并完整携带目标规则字段，再把出站目的改为域名；域名目的使用 HTTPS 等应用层协议。

Input: 

```
tccli cfw ModifyAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent example.com \
    --Rules.0.TargetType domain \
    --Rules.0.Protocol HTTPS \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 3118 \
    --Rules.0.Uuid 246813 \
    --Rules.0.Enable false \
    --Rules.0.Description 观察文档域名 HTTPS 访问 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0 \
    --Rules.0.LogId  \
    --Rules.0.ParamTemplateId 
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            246813
        ],
        "RequestId": "00000000-0000-4000-8000-000000000004"
    }
}
```

