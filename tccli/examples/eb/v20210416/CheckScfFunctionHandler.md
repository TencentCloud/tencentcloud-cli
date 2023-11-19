**Example 1: 检验scf函数**



Input: 

```
tccli eb CheckScfFunctionHandler --cli-unfold-argument  \
    --EventBusId rule-xxxxxx \
    --RuleId rule-xxxxxx \
    --Type scf \
    --ResourceDescription qcs::scf_custom:ap-guangzhou:uin/xxxxxxxx:namespace/xxxxxx/function/xxxxx/x
```

Output: 
```
{
    "Response": {
        "CheckResult": true,
        "RequestId": "b7662cf2-ce20-4b3e-aff2-2cb875cf0b6b"
    }
}
```

