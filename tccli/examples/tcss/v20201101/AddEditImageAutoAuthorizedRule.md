**Example 1: 新增或编辑本地镜像自动授权规则**



Input: 

```
tccli tcss AddEditImageAutoAuthorizedRule --cli-unfold-argument  \
    --RangeType "MANUAL" \
    --HostIdSet "xx" \
    --MaxDailyCount 1 \
    --RuleId 1 \
    --IsEnabled 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

