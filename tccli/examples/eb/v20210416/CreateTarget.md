**Example 1: 创建目标**



Input: 

```
tccli eb CreateTarget --cli-unfold-argument  \
    --EventBusId eb-l65vlc2 \
    --Type scf \
    --TargetDescription.ResourceDescription qcs::scf:ap-guanzhou:uin/3473058547:namespace/default/function/test/1 \
    --RuleId rule-fdltium8
```

Output: 
```
{
    "Response": {
        "RequestId": "b7662cf2-ce20-4b3e-aff2-2cb875cf0b6b",
        "TargetId": "target-o5yx01oq"
    }
}
```

