**Example 1: 修改单条白名单策略**

将 DescribeWhiteRule.Data[].WhiteId 写入 Rule.Info.WhiteId；单值 Rule.Info 更新原策略，本示例保留匹配条件并延长有效期。

Input: 

```
tccli cfw ModifyWhiteRule --cli-unfold-argument  \
    --Rule.RuleName 办公出口 IP 加白 \
    --Rule.FwType 1 \
    --Rule.Comment 延长有效期 \
    --Rule.EndTime 2099-01-01 00:00:00 \
    --Rule.Info.SrcIP 198.51.100.201 \
    --Rule.Info.WhiteId wl-xxxxxxxx \
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

