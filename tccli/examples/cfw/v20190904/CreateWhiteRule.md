**Example 1: 创建精确源 IP 白名单**

RuleType=2；Rules[].Info.SrcIP、DstIP 两个字段中恰好填写一个，CoverDuplicate 可省略。

Input: 

```
tccli cfw CreateWhiteRule --cli-unfold-argument  \
    --Rules.0.RuleName 办公出口 IP 加白 \
    --Rules.0.FwType 31 \
    --Rules.0.Comment 可信办公出口 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Info.SrcIP 198.51.100.201 \
    --RuleType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 创建域名白名单**

RuleType=3，域名填写 Rules[].Info.Ioc。

Input: 

```
tccli cfw CreateWhiteRule --cli-unfold-argument  \
    --Rules.0.RuleName 可信业务域名 \
    --Rules.0.FwType 31 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Info.Ioc api.example.com \
    --RuleType 3
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 3: 创建 CIDR 扩展白名单**

RuleType=8 用于 CIDR/端口/组合；精确单 IP 用 RuleType=2。

Input: 

```
tccli cfw CreateWhiteRule --cli-unfold-argument  \
    --Rules.0.RuleName 可信源网段 \
    --Rules.0.FwType 2 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Info.SrcIP 198.51.100.0/30 \
    --RuleType 8
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 4: 创建 NDR User-Agent 白名单**

RuleType=9 且 FwType=16；多 UA 用 <#cfw-splite#>。

Input: 

```
tccli cfw CreateWhiteRule --cli-unfold-argument  \
    --Rules.0.RuleName 可信扫描器 UA \
    --Rules.0.FwType 16 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Info.UserAgent TrustedScanner/1.0 \
    --RuleType 9
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

