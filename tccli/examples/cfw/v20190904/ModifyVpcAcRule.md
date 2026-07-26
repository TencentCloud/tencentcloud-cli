**Example 1: 修改一条 IPv4 VPC 规则**

将 Uuid 指定的 VPC 规则修改为拒绝。

Input: 

```
tccli cfw ModifyVpcAcRule --cli-unfold-argument  \
    --Rules.0.Uuid 246810 \
    --Rules.0.SourceType net \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.DestType net \
    --Rules.0.DestContent 198.51.100.0/24 \
    --Rules.0.Protocol TCP \
    --Rules.0.Port 443 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.RuleAction drop \
    --Rules.0.Description Documented service traffic policy \
    --Rules.0.OrderIndex 12 \
    --Rules.0.Enable true \
    --Rules.0.EdgeId ALL \
    --Rules.0.FwGroupId ALL \
    --Rules.0.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            246810
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174000"
    }
}
```

**Example 2: 修改一条 IPv6 VPC 规则**

先查询并确认规则的完整 IPv6 配置，再按完整字段重建规则；示例保持 IPv6 地址版本并修改为观察动作。

Input: 

```
tccli cfw ModifyVpcAcRule --cli-unfold-argument  \
    --Rules.0.Uuid 246812 \
    --Rules.0.SourceType net \
    --Rules.0.SourceContent 2001:db8:1::/64 \
    --Rules.0.DestType net \
    --Rules.0.DestContent 2001:db8:2::/64 \
    --Rules.0.Protocol UDP \
    --Rules.0.Port 53 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.RuleAction log \
    --Rules.0.Description 观察 IPv6 VPC DNS 流量 \
    --Rules.0.OrderIndex 13 \
    --Rules.0.Enable true \
    --Rules.0.EdgeId ALL \
    --Rules.0.FwGroupId ALL \
    --Rules.0.IpVersion 1
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            246812
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174001"
    }
}
```

**Example 3: 将 VPC 规则修改为协议端口模板规则**

使用协议端口模板修改 Uuid 指定的 VPC 规则。

Input: 

```
tccli cfw ModifyVpcAcRule --cli-unfold-argument  \
    --Rules.0.Uuid 246814 \
    --Rules.0.SourceType net \
    --Rules.0.SourceContent 192.0.2.130 \
    --Rules.0.DestType net \
    --Rules.0.DestContent 198.51.100.130 \
    --Rules.0.Protocol ANY \
    --Rules.0.Port -1/-1 \
    --Rules.0.ParamTemplateId pp-maatbnad \
    --Rules.0.RuleAction log \
    --Rules.0.Description VPC 协议端口模板观察规则 \
    --Rules.0.OrderIndex 2 \
    --Rules.0.Enable false \
    --Rules.0.EdgeId cfws-b29ca53311 \
    --Rules.0.FwGroupId ALL \
    --Rules.0.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            246814
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174002"
    }
}
```

**Example 4: 将 VPC 规则修改为实例访问严格匹配域名**

用户要求指定实例仅在域名和解析 IP 同时匹配时访问外部服务。先调用 DescribeCfwRules 查询目标规则的完整字段，调用 DescribeCfwAssets 获取来源 assets[].instance_id，再将目的类型改为 domainiptwoverify。

Input: 

```
tccli cfw ModifyVpcAcRule --cli-unfold-argument  \
    --Rules.0.Uuid 246815 \
    --Rules.0.SourceType instance \
    --Rules.0.SourceContent ins-xxxxxxxx \
    --Rules.0.DestType domainiptwoverify \
    --Rules.0.DestContent example.org \
    --Rules.0.Protocol TCP \
    --Rules.0.Port 443 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.RuleAction log \
    --Rules.0.Description 观察实例访问严格匹配域名 \
    --Rules.0.OrderIndex 11 \
    --Rules.0.Enable false \
    --Rules.0.EdgeId ALL \
    --Rules.0.FwGroupId ALL \
    --Rules.0.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            246815
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174003"
    }
}
```

