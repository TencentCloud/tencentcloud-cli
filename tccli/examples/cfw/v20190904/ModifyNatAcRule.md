**Example 1: 修改一条NAT出站访问控制规则**

将 Uuid 指定的 NAT 规则修改为放行。

Input: 

```
tccli cfw ModifyNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.10/32 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.20/32 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 8 \
    --Rules.0.Uuid 90010001 \
    --Rules.0.Enable true \
    --Rules.0.Description 允许文档示例HTTPS流量 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            90010001
        ],
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 修改一条 NAT 入站访问控制规则**

先查询并确认 Uuid 对应的入站规则，再按完整字段重建规则；示例保持入站方向并修改为观察动作。

Input: 

```
tccli cfw ModifyNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.30 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 8443 \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex 9 \
    --Rules.0.Uuid 90010002 \
    --Rules.0.Enable true \
    --Rules.0.Description 观察 NAT 入站示例流量 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            90010002
        ],
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

**Example 3: 按用户要求将规则修改为观察访问腾讯云的出站流量**

用户要求“将规则修改为观察访问腾讯云的出站流量”时，先调用 DescribeCfwRules 查询目标规则并完整携带其可写字段，再把出站目的改为 vendor 和协议值 tencent；不得把展示名称“腾讯云”写入 TargetContent。

Input: 

```
tccli cfw ModifyNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent tencent \
    --Rules.0.TargetType vendor \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction log \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 10 \
    --Rules.0.Uuid 90010004 \
    --Rules.0.Enable false \
    --Rules.0.Description 观察访问腾讯云的出站流量 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            90010004
        ],
        "RequestId": "00000000-0000-4000-8000-000000000004"
    }
}
```

**Example 4: 将 NAT 规则修改为地址模板规则**

使用地址模板修改 Uuid 指定的 NAT 规则。

Input: 

```
tccli cfw ModifyNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.120 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent mb_xxxxx_xxxxx \
    --Rules.0.TargetType template \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1066 \
    --Rules.0.Uuid 90010003 \
    --Rules.0.Enable false \
    --Rules.0.Description NAT 地址模板观察规则 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.Scope ALL
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            90010003
        ],
        "RequestId": "00000000-0000-4000-8000-000000000003"
    }
}
```

