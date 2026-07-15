**Example 1: 批量自定义规则开关接口**



Input: 

```
tccli waf ModifyBatchCustomRuleStatus --cli-unfold-argument  \
    --Id 11101 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "Res": "success",
        "RequestId": "324b0821-ea0a-e071-3d26-4147c7fdc93e"
    }
}
```

