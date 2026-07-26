**Example 1: 添加一条出站互联网边界观察规则**

使用 RFC 5737 文档地址添加一条出站串行 TCP 观察规则；显式指定启用状态、生效范围、规则来源和末尾优先级。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.10 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.Description 出站 TCP 观察示例 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
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

**Example 2: 添加一条入站地域来源规则**

添加一条入站串行 TCP 规则，来源使用地域 code；地域 code 应通过只读查询取得，示例中的 gd44 仅用于展示格式。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent gd44 \
    --Rules.0.SourceType location \
    --Rules.0.TargetContent 198.51.100.0/24 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port 443 \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.Description 允许地域来源访问 HTTPS \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
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

**Example 3: 插入一条旁路互联网边界规则**

使用 insert_rule 在指定位置插入一条禁用的出站旁路规则；调用前使用 DescribeCfwRules，传 RuleType=border、Direction=0、ExpandNames=false，将目标位置对应的 rules[].sequence 写入 OrderIndex。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --From insert_rule \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.10 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 3118 \
    --Rules.0.Enable false \
    --Rules.0.Description 插入旁路观察规则 \
    --Rules.0.Scope side \
    --Rules.0.RuleSource 0
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

**Example 4: 在连续位置批量插入互联网边界规则**

两条规则使用相同的 Direction，并按请求顺序将 OrderIndex 设置为连续位置 3 和 4。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --From insert_rule \
    --Rules.0.SourceContent 192.0.2.31 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.31 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 3 \
    --Rules.0.Enable false \
    --Rules.0.Description 连续位置批量插入示例一 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0 \
    --Rules.1.SourceContent 192.0.2.32 \
    --Rules.1.SourceType net \
    --Rules.1.TargetContent 198.51.100.32 \
    --Rules.1.TargetType net \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 8443 \
    --Rules.1.Direction 0 \
    --Rules.1.OrderIndex 4 \
    --Rules.1.Enable false \
    --Rules.1.Description 连续位置批量插入示例二 \
    --Rules.1.Scope serial \
    --Rules.1.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100008,
            100009
        ],
        "RequestId": "00000000-0000-4000-8000-000000000008"
    }
}
```

**Example 5: 批量导入两条全局互联网边界规则**

使用非覆盖的 batch_import 新增两条禁用的出站全局规则；该方式不会删除已有规则。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --From batch_import \
    --Rules.0.SourceContent 192.0.2.1 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.31 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 批量全局规则一 \
    --Rules.0.Scope all \
    --Rules.0.RuleSource 0 \
    --Rules.1.SourceContent 192.0.2.2 \
    --Rules.1.SourceType net \
    --Rules.1.TargetContent 198.51.100.32 \
    --Rules.1.TargetType net \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 8443 \
    --Rules.1.Direction 0 \
    --Rules.1.OrderIndex -1 \
    --Rules.1.Enable false \
    --Rules.1.Description 批量全局规则二 \
    --Rules.1.Scope all \
    --Rules.1.RuleSource 0
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

**Example 6: 使用地址模板新增互联网边界规则**

使用地址模板新增一条互联网边界规则。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent mb_xxxxx_xxxxx \
    --Rules.0.SourceType template \
    --Rules.0.TargetContent 198.51.100.60 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 地址模板观察规则 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
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

**Example 7: 使用资源标签新增互联网边界规则**

调用 DescribeResourceGroupNew，传 QueryType=tag，以一级节点 GroupName 为 Key、所选二级子节点 GroupName 为 Value 构造访问源。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent {"Key":"自动化测试","Value":"autotest"} \
    --Rules.0.SourceType tag \
    --Rules.0.TargetContent 198.51.100.60 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 资源标签观察规则 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
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

**Example 8: 允许腾讯云来源访问指定资产**

用户要求允许腾讯云来源访问指定资产时，先调用 DescribeCfwAssets，选择具有公网 IP 的目标资产并使用 assets[].instance_id；云厂商使用协议值 tencent，不要填写展示名称“腾讯云”。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent tencent \
    --Rules.0.SourceType vendor \
    --Rules.0.TargetContent ins-xxxxxxxx \
    --Rules.0.TargetType instance \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction log \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 观察腾讯云来源访问指定资产 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100010
        ],
        "RequestId": "00000000-0000-4000-8000-000000000010"
    }
}
```

**Example 9: 添加 DNS 宽松和严格匹配规则**

用户要求按域名解析结果控制出站访问时，可在同一方向批量添加两条规则：dnsparse 在 Host/SNI 匹配或目的 IP 属于当前 DNS 解析结果时命中，domainiptwoverify 要求两个条件同时满足。两条规则均使用查询或用户确认的精确域名，不使用单独的 *。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent example.com \
    --Rules.0.TargetType dnsparse \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 观察 DNS 宽松匹配流量 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0 \
    --Rules.1.SourceContent 192.0.2.0/24 \
    --Rules.1.SourceType net \
    --Rules.1.TargetContent example.org \
    --Rules.1.TargetType domainiptwoverify \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 443 \
    --Rules.1.Direction 0 \
    --Rules.1.OrderIndex -1 \
    --Rules.1.Enable false \
    --Rules.1.Description 观察 DNS 严格匹配流量 \
    --Rules.1.Scope serial \
    --Rules.1.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100011,
            100012
        ],
        "RequestId": "00000000-0000-4000-8000-000000000011"
    }
}
```

