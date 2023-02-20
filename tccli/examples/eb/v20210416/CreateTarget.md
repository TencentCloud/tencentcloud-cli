**Example 1: 创建目标**



Input: 

```
tccli eb CreateTarget --cli-unfold-argument  \
    --EventBusId eb-xxxxxx \
    --Type scf \
    --TargetDescription.ResourceDescription qcs::scf:ap-guangzhou:uin/xxxxxxxx:namespace/xxxxxx/function/xxxxx/x \
    --RuleId rule-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b7662cf2-ce20-4b3e-aff2-2cb875cf0b6b",
        "TargetId": "target-xxxxxx"
    }
}
```

