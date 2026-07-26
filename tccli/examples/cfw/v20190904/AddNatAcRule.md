**Example 1: 普通新增 NAT 出站观察规则**

新增一条出站观察规则。

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent example.com \
    --Rules.0.TargetType domain \
    --Rules.0.Protocol HTTP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 80 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Enable true \
    --Rules.0.Description 观察文档站点 HTTP \
    --Rules.0.Scope cfwnat-example0001
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100001
        ],
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 普通新增 NAT 入站规则**

新增一条作用于全部 NAT 实例的入站 TCP 放行规则，使用 RFC 5737 文档地址展示 net 类型。

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.10 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port 443 \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.Description 允许入站 HTTPS 示例 \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100002
        ],
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

**Example 3: 插入一条 NAT 访问控制规则**

使用 insert_rule 在指定位置插入一条禁用的出站规则；调用前使用 DescribeCfwRules，传 RuleType=nat、Direction=0、ExpandNames=false，将目标位置对应的 rules[].sequence 写入 OrderIndex。

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --From insert_rule \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.20 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 8443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1066 \
    --Rules.0.Enable false \
    --Rules.0.Description 插入 NAT 观察规则 \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100003
        ],
        "RequestId": "00000000-0000-4000-8000-000000000003"
    }
}
```

**Example 4: 批量导入两条 NAT 规则**

使用非覆盖的 batch_import 新增两条禁用的出站规则；该方式不会删除已有规则。

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --From batch_import \
    --Rules.0.SourceContent 192.0.2.41 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.41 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 批量 NAT 规则一 \
    --Rules.0.Scope ALL \
    --Rules.1.SourceContent 192.0.2.42 \
    --Rules.1.SourceType net \
    --Rules.1.TargetContent 198.51.100.42 \
    --Rules.1.TargetType net \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 8443 \
    --Rules.1.Direction 0 \
    --Rules.1.OrderIndex -1 \
    --Rules.1.Enable false \
    --Rules.1.Description 批量 NAT 规则二 \
    --Rules.1.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100004,
            100005
        ],
        "RequestId": "00000000-0000-4000-8000-000000000004"
    }
}
```

**Example 5: 使用协议端口模板新增 NAT 规则**

使用协议端口模板新增一条 NAT 规则。

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.70 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.70 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction log \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 协议端口模板观察规则 \
    --Rules.0.ParamTemplateId pp-maatbnad \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100006
        ],
        "RequestId": "00000000-0000-4000-8000-000000000005"
    }
}
```

**Example 6: 观察广东来源访问指定实例**

用户要求观察广东来源访问指定实例时，调用 DescribeAclRegInfo，传 FwType=["NAT"]，从 Data 中匹配 RegionName=广东省并使用 RegionCode=gd44；调用 DescribeCfwAssets 获取目标 assets[].instance_id。

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent gd44 \
    --Rules.0.SourceType location \
    --Rules.0.TargetContent ins-xxxxxxxx \
    --Rules.0.TargetType instance \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction log \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 观察广东来源访问指定实例 \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100007
        ],
        "RequestId": "00000000-0000-4000-8000-000000000006"
    }
}
```

**Example 7: 添加实例出站 DNS 宽松和严格匹配规则**

用户要求实例按域名解析结果访问外部服务时，调用 DescribeCfwAssets 获取来源 assets[].instance_id。dnsparse 在 Host/SNI 匹配或目的 IP 属于当前 DNS 解析结果时命中，domainiptwoverify 要求两个条件同时满足。

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent ins-xxxxxxxx \
    --Rules.0.SourceType instance \
    --Rules.0.TargetContent example.com \
    --Rules.0.TargetType dnsparse \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 观察实例 DNS 宽松匹配流量 \
    --Rules.0.Scope ALL \
    --Rules.1.SourceContent ins-xxxxxxxx \
    --Rules.1.SourceType instance \
    --Rules.1.TargetContent example.org \
    --Rules.1.TargetType domainiptwoverify \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 443 \
    --Rules.1.Direction 0 \
    --Rules.1.OrderIndex -1 \
    --Rules.1.Enable false \
    --Rules.1.Description 观察实例 DNS 严格匹配流量 \
    --Rules.1.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100008,
            100009
        ],
        "RequestId": "00000000-0000-4000-8000-000000000007"
    }
}
```

