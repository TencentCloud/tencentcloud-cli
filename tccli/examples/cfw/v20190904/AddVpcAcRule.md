**Example 1: 普通新增 IPv4 VPC 规则**

使用 RFC 5737 文档地址新增一条启用的 IPv4 TCP 规则；省略 From 表示普通新增。

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.10 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent 198.51.100.20 \
    --Rules.0.DestType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port 443 \
    --Rules.0.Description 允许文档网段 HTTPS 访问 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.EdgeId ALL \
    --Rules.0.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            10001
        ],
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 普通新增 IPv6 VPC 规则**

使用 RFC 3849 文档地址新增一条启用的 IPv6 UDP 规则；省略 From 表示普通新增。

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 2001:db8:1::10 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent 2001:db8:2::20 \
    --Rules.0.DestType net \
    --Rules.0.Protocol UDP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 53 \
    --Rules.0.Description 观察文档网段 DNS 访问 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.EdgeId ALL \
    --Rules.0.IpVersion 1
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            10002
        ],
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

**Example 3: 普通新增 VPC 域名访问规则**

新增一条 IPv4 VPC 域名观察规则；域名目的使用应用层协议，省略 From 表示普通新增。

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent example.com \
    --Rules.0.DestType domain \
    --Rules.0.Protocol HTTP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 80 \
    --Rules.0.Description 观察 VPC 到文档域名的 HTTP 访问 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.EdgeId ALL \
    --Rules.0.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            10003
        ],
        "RequestId": "00000000-0000-4000-8000-000000000003"
    }
}
```

**Example 4: 在指定 VPC 边插入规则**

使用 insert_rule 在指定 VPC 边插入一条禁用规则。

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --From insert_rule \
    --Rules.0.SourceContent 192.0.2.10 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent 198.51.100.10 \
    --Rules.0.DestType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Description 指定 VPC 边插入规则 \
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
            10004
        ],
        "RequestId": "00000000-0000-4000-8000-000000000004"
    }
}
```

**Example 5: 在指定防火墙组批量导入 VPC 规则**

使用非覆盖的 batch_import 向指定防火墙组新增两条禁用规则。

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --From batch_import \
    --Rules.0.SourceContent 192.0.2.51 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent 198.51.100.51 \
    --Rules.0.DestType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Description 批量 VPC 规则一 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.EdgeId ALL \
    --Rules.0.FwGroupId cfwg-8f6785ee \
    --Rules.0.IpVersion 0 \
    --Rules.1.SourceContent 192.0.2.52 \
    --Rules.1.SourceType net \
    --Rules.1.DestContent 198.51.100.52 \
    --Rules.1.DestType net \
    --Rules.1.Protocol UDP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 53 \
    --Rules.1.Description 批量 VPC 规则二 \
    --Rules.1.OrderIndex -1 \
    --Rules.1.Enable false \
    --Rules.1.EdgeId ALL \
    --Rules.1.FwGroupId cfwg-8f6785ee \
    --Rules.1.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            10005,
            10006
        ],
        "RequestId": "00000000-0000-4000-8000-000000000005"
    }
}
```

**Example 6: 添加实例访问域名的 DNS 宽松和严格匹配规则**

用户要求指定实例按域名解析结果访问外部服务时，调用 DescribeCfwAssets 获取来源 assets[].instance_id。dnsparse 在 Host/SNI 匹配或目的 IP 属于当前 DNS 解析结果时命中，domainiptwoverify 要求两个条件同时满足。

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent ins-xxxxxxxx \
    --Rules.0.SourceType instance \
    --Rules.0.DestContent example.com \
    --Rules.0.DestType dnsparse \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Description 观察实例 DNS 宽松匹配流量 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.EdgeId ALL \
    --Rules.0.IpVersion 0 \
    --Rules.1.SourceContent ins-xxxxxxxx \
    --Rules.1.SourceType instance \
    --Rules.1.DestContent example.org \
    --Rules.1.DestType domainiptwoverify \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 443 \
    --Rules.1.Description 观察实例 DNS 严格匹配流量 \
    --Rules.1.OrderIndex -1 \
    --Rules.1.Enable false \
    --Rules.1.EdgeId ALL \
    --Rules.1.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            10007,
            10008
        ],
        "RequestId": "00000000-0000-4000-8000-000000000006"
    }
}
```

**Example 7: 添加资源标签访问网段的 VPC 规则**

用户要求一组带标签的资产访问指定网段时，调用 DescribeResourceGroupNew，传 QueryType=tag，以一级节点 GroupName 为 Key、所选二级子节点 GroupName 为 Value 构造 SourceContent。

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent {"Key":"environment","Value":"production"} \
    --Rules.0.SourceType tag \
    --Rules.0.DestContent 10.0.0.0/24 \
    --Rules.0.DestType net \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction log \
    --Rules.0.Port -1/-1 \
    --Rules.0.Description 观察指定标签资产访问目标网段 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.EdgeId ALL \
    --Rules.0.IpVersion 0
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            10009
        ],
        "RequestId": "00000000-0000-4000-8000-000000000007"
    }
}
```

