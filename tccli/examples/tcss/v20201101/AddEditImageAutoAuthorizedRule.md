**Example 1: 新增或编辑本地镜像自动授权规则**



Input: 

```
tccli tcss AddEditImageAutoAuthorizedRule --cli-unfold-argument  \
    --RangeType "MANUAL" \
    --HostIdSet "be119857-7949-4650-aef5-9591b54091d0" \
    --MaxDailyCount 1 \
    --RuleId 1 \
    --IsEnabled 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c826b9fa-68b5-4603-bf25-a5eb9b65c768"
    }
}
```

