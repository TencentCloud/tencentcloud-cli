**Example 1: 添加漏洞忽略规则**

添加漏洞忽略规则

Input: 

```
tccli cwp AddVulIgnoreRule --cli-unfold-argument  \
    --RuleDetailList.0.VulID 50 \
    --RuleDetailList.0.AssetScopeType 0 \
    --RuleDetailList.0.Remark test1
```

Output: 
```
{
    "Response": {
        "RequestId": "300d942e-df84-48b8-b7ee-bc0000852863"
    }
}
```

