**Example 1: 使用协议和端口新增企业安全组规则**

显式指定 TCP 协议和 443 端口，在最高优先级新增一条放行规则。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 1 \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.0.2.0/24 \
    --Data.0.DestType net \
    --Data.0.DestContent 198.51.100.10 \
    --Data.0.RuleAction accept \
    --Data.0.Description 允许文档网段访问 HTTPS \
    --Data.0.OrderIndex 1 \
    --Data.0.Protocol TCP \
    --Data.0.Port 443 \
    --Data.0.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "SourceContent": "192.0.2.0/24",
                "DestContent": "198.51.100.10",
                "Protocol": "TCP",
                "Description": "允许文档网段访问 HTTPS",
                "RuleUuid": 900001,
                "Sequence": 1,
                "Scope": "SG"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174000"
    }
}
```

**Example 2: 使用服务模板新增企业安全组规则**

使用服务模板新增企业安全组规则。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 1 \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.0.2.0/24 \
    --Data.0.DestType net \
    --Data.0.DestContent 198.51.100.20 \
    --Data.0.RuleAction drop \
    --Data.0.Description 使用服务模板限制文档地址 \
    --Data.0.OrderIndex 1 \
    --Data.0.Protocol ANY \
    --Data.0.Port -1/-1 \
    --Data.0.ServiceTemplateId ppmg-example-service-01 \
    --Data.0.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "SourceContent": "192.0.2.0/24",
                "DestContent": "198.51.100.20",
                "Protocol": "ANY",
                "Description": "使用服务模板限制文档地址",
                "RuleUuid": 900002,
                "Sequence": 1,
                "Scope": "SG"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174001"
    }
}
```

**Example 3: 在末尾新增轻量服务器范围规则**

使用 Type=0 在末尾新增一条 LH 范围规则；LH 范围不能使用地址模板或服务模板。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 0 \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.0.2.0/24 \
    --Data.0.DestType net \
    --Data.0.DestContent 198.51.100.30 \
    --Data.0.RuleAction accept \
    --Data.0.Description 允许轻量服务器 HTTPS 访问 \
    --Data.0.OrderIndex -1 \
    --Data.0.Protocol TCP \
    --Data.0.Port 443 \
    --Data.0.Scope LH
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "SourceContent": "192.0.2.0/24",
                "DestContent": "198.51.100.30",
                "Protocol": "TCP",
                "Description": "允许轻量服务器 HTTPS 访问",
                "RuleUuid": 900003,
                "Sequence": 3,
                "Scope": "LH"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174002"
    }
}
```

**Example 4: 在指定位置插入企业安全组规则**

使用 Type=2 在指定顺序插入一条规则，并通过 IsDelay=1 延迟生效；调用前使用 DescribeCfwRules，传 RuleType=enterprise_sg、ExpandNames=false，将目标位置对应的 rules[].sequence 转为十进制字符串后写入 OrderIndex。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 2 \
    --IsDelay 1 \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.0.2.80 \
    --Data.0.DestType net \
    --Data.0.DestContent 198.51.100.80 \
    --Data.0.RuleAction accept \
    --Data.0.Description 指定位置企业安全组规则 \
    --Data.0.OrderIndex 7 \
    --Data.0.Protocol TCP \
    --Data.0.Port 443 \
    --Data.0.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "RuleUuid": 900004,
                "Sequence": 7,
                "SourceContent": "192.0.2.80",
                "DestContent": "198.51.100.80",
                "Protocol": "TCP",
                "Description": "指定位置企业安全组规则",
                "Scope": "SG"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174003"
    }
}
```

**Example 5: 批量导入企业安全组规则**

使用非覆盖的 batch_import 新增两条禁用规则，并通过 IsDelay=1 延迟生效；不会删除已有规则。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 0 \
    --From batch_import \
    --IsDelay 1 \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.0.2.91 \
    --Data.0.DestType net \
    --Data.0.DestContent 198.51.100.91 \
    --Data.0.RuleAction accept \
    --Data.0.Description 批量企业安全组规则一 \
    --Data.0.OrderIndex -1 \
    --Data.0.Protocol TCP \
    --Data.0.Port 443 \
    --Data.0.Enable false \
    --Data.0.Scope SG \
    --Data.1.SourceType net \
    --Data.1.SourceContent 192.0.2.92 \
    --Data.1.DestType net \
    --Data.1.DestContent 198.51.100.92 \
    --Data.1.RuleAction accept \
    --Data.1.Description 批量企业安全组规则二 \
    --Data.1.OrderIndex -1 \
    --Data.1.Protocol UDP \
    --Data.1.Port 53 \
    --Data.1.Enable false \
    --Data.1.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "RuleUuid": 900005,
                "Sequence": 8,
                "SourceContent": "192.0.2.91",
                "DestContent": "198.51.100.91",
                "Protocol": "TCP",
                "Description": "批量企业安全组规则一",
                "Scope": "SG"
            },
            {
                "RuleUuid": 900006,
                "Sequence": 9,
                "SourceContent": "192.0.2.92",
                "DestContent": "198.51.100.92",
                "Protocol": "UDP",
                "Description": "批量企业安全组规则二",
                "Scope": "SG"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174004"
    }
}
```

**Example 6: 延迟下发企业安全组规则**

使用 IsDelay=1 将规则保留为待生效状态，后续需由业务流程显式发布。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 0 \
    --IsDelay 1 \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.0.2.100 \
    --Data.0.DestType net \
    --Data.0.DestContent 198.51.100.100 \
    --Data.0.RuleAction accept \
    --Data.0.Description 延迟下发企业安全组规则 \
    --Data.0.OrderIndex -1 \
    --Data.0.Protocol TCP \
    --Data.0.Port 9443 \
    --Data.0.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "RuleUuid": 900007,
                "Sequence": 10,
                "SourceContent": "192.0.2.100",
                "DestContent": "198.51.100.100",
                "Protocol": "TCP",
                "Description": "延迟下发企业安全组规则",
                "Scope": "SG"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174005"
    }
}
```

**Example 7: 新增安全组和轻量服务器组合范围规则**

使用 SG,LH 组合范围同时作用于安全组和轻量服务器；组合范围不能使用地址模板或服务模板。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 0 \
    --IsDelay 1 \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.0.2.110 \
    --Data.0.DestType net \
    --Data.0.DestContent 198.51.100.110 \
    --Data.0.RuleAction accept \
    --Data.0.Description 安全组和轻量服务器组合范围 \
    --Data.0.OrderIndex -1 \
    --Data.0.Protocol TCP \
    --Data.0.Port 443 \
    --Data.0.Scope SG,LH
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "RuleUuid": 900008,
                "Sequence": 11,
                "SourceContent": "192.0.2.110",
                "DestContent": "198.51.100.110",
                "Protocol": "TCP",
                "Description": "安全组和轻量服务器组合范围",
                "Scope": "SG,LH"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174006"
    }
}
```

**Example 8: 批量添加标签地域和实例域名规则**

用户要求按资产标签限制访问地域，并允许指定实例按 DNS 解析结果访问域名时，调用 DescribeResourceGroupNew 获取标签名称，调用 DescribeSecurityGroupRegionList 获取 Data[].Region，调用 DescribeCfwAssets 获取 assets[].instance_id。

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Type 0 \
    --From batch_import \
    --IsDelay 1 \
    --Data.0.SourceType tag \
    --Data.0.SourceContent {"Key":"environment","Value":"production"} \
    --Data.0.DestType region \
    --Data.0.DestContent ap-guangzhou \
    --Data.0.RuleAction log \
    --Data.0.Description 观察生产标签资产访问广州地域 \
    --Data.0.OrderIndex -1 \
    --Data.0.Protocol ANY \
    --Data.0.Port -1/-1 \
    --Data.0.Enable false \
    --Data.0.Scope SG \
    --Data.1.SourceType instance \
    --Data.1.SourceContent ins-xxxxxxxx \
    --Data.1.DestType dnsparse \
    --Data.1.DestContent example.com \
    --Data.1.RuleAction log \
    --Data.1.Description 观察指定实例访问解析域名 \
    --Data.1.OrderIndex -1 \
    --Data.1.Protocol TCP \
    --Data.1.Port 443 \
    --Data.1.Enable false \
    --Data.1.Scope SG
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Rules": [
            {
                "RuleUuid": 900009,
                "Sequence": 12,
                "SourceContent": "{\"Key\":\"environment\",\"Value\":\"production\"}",
                "DestContent": "ap-guangzhou",
                "Protocol": "ANY",
                "Description": "观察生产标签资产访问广州地域",
                "Scope": "SG"
            },
            {
                "RuleUuid": 900010,
                "Sequence": 13,
                "SourceContent": "ins-xxxxxxxx",
                "DestContent": "example.com",
                "Protocol": "TCP",
                "Description": "观察指定实例访问解析域名",
                "Scope": "SG"
            }
        ],
        "RequestId": "123e4567-e89b-42d3-a456-426614174007"
    }
}
```

