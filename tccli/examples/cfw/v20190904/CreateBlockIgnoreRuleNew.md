**Example 1: 新增永久 IP 封禁规则**

将一个 RFC 5737 文档地址添加到互联网出站封禁列表；不覆盖已有冲突规则。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 192.0.2.10 \
    --Rules.0.DirectionList 0 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 永久 IP 封禁示例 \
    --RuleType 1 \
    --CoverDuplicate 0
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 新增双向永久 IP 封禁规则**

双向封禁一个 IP，DirectionList 传 "1,0"，同时阻断互联网入向和出向流量。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 192.0.2.10 \
    --Rules.0.DirectionList 1,0 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 双向永久封禁示例 \
    --RuleType 1 \
    --CoverDuplicate 0
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

**Example 3: 新增 IP 封禁并替换互斥规则**

新增一条出站封禁规则；如放通列表中已有同 IP、同方向规则，CoverDuplicate=1 会保留本次封禁并删除冲突放通规则。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 203.0.113.20 \
    --Rules.0.DirectionList 0 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 替换互斥规则示例 \
    --RuleType 1 \
    --CoverDuplicate 1
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000005"
    }
}
```

**Example 4: 批量新增定时 IP 封禁规则**

在一次请求中新增两条仅入站定时封禁规则；每条规则独立指定 IOC、方向和结束时间，不覆盖已有冲突规则。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 192.0.2.211 \
    --Rules.0.DirectionList 1 \
    --Rules.0.EndTime 2099-01-01 00:00:00 \
    --Rules.0.Comment 批量定时封禁示例一 \
    --Rules.1.Ioc 192.0.2.212 \
    --Rules.1.DirectionList 1 \
    --Rules.1.EndTime 2099-01-02 00:00:00 \
    --Rules.1.Comment 批量定时封禁示例二 \
    --RuleType 1 \
    --CoverDuplicate 0
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000004"
    }
}
```

**Example 5: 新增 IP 放通规则**

将一个 RFC 5737 文档地址添加到互联网入站放通列表；不覆盖已有冲突规则。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 192.0.2.20 \
    --Rules.0.DirectionList 1 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment IP 放通示例 \
    --RuleType 2 \
    --CoverDuplicate 0
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000008"
    }
}
```

**Example 6: 新增域名放通规则**

新增一条互联网出站域名放通规则。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc example.com \
    --Rules.0.DirectionList 0 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 域名放通示例 \
    --RuleType 3
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000006"
    }
}
```

**Example 7: 新增情报放通规则**

将一个 IP 情报对象添加到互联网出入站放通列表。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 192.0.2.40 \
    --Rules.0.DirectionList 1,0 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 情报放通示例 \
    --RuleType 4
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000009"
    }
}
```

**Example 8: 新增资产放通规则**

将 DescribeCfwAssets 返回的一个 CVM 实例添加到内网源和内网目的放通列表；Ioc 应替换为当前账号 assets[].instance_id。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc ins-xxxxxxxx \
    --Rules.0.DirectionList 5,6 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 资产放通示例 \
    --RuleType 5
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000010"
    }
}
```

**Example 9: 新增自定义放通规则**

新增一条私网源到私网目的的 VPC 防火墙自定义放通规则。Ioc 必须显式传空字符串，DirectionList 必须显式传非空值；IdsRuleId 应替换为 DescribeIpsRuleListNew 返回的现有规则 ID。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc  \
    --Rules.0.DirectionList 5,6 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 自定义放通规则示例 \
    --Rules.0.FwType 4 \
    --Rules.0.CustomRule.SrcIP 10.0.0.11 \
    --Rules.0.CustomRule.DstIP 10.0.0.12 \
    --Rules.0.CustomRule.IdsRuleId 20001 \
    --Rules.0.CustomRule.IdsRuleName 自定义放通规则示例 \
    --RuleType 6 \
    --CoverDuplicate 0
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000007"
    }
}
```

**Example 10: 新增多引擎自定义放通规则**

用户要求同一条自定义策略应用于互联网边界、NAT 和 VPC 防火墙时，调用 DescribeCfwAssets 取资产 IP 作为 SrcIP，调用 DescribeIpsRuleListNew 取 Data[].RuleID；FwType=15 表示请求旁路、NAT、VPC 和串行引擎，服务会按源和目的地址实际适用的引擎收窄。

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc  \
    --Rules.0.DirectionList 1,0 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 多引擎自定义放通规则 \
    --Rules.0.FwType 15 \
    --Rules.0.CustomRule.SrcIP 10.0.0.10 \
    --Rules.0.CustomRule.DstIP 198.51.100.20 \
    --Rules.0.CustomRule.IdsRuleId 20001 \
    --Rules.0.CustomRule.IdsRuleName 多引擎自定义放通规则 \
    --RuleType 6 \
    --CoverDuplicate 0
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000011"
    }
}
```

