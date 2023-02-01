**Example 1: 解封限速实例**

解封限速实例

Input: 

```
tccli vpc UnlockCcnBandwidths --cli-unfold-argument  \
    --Instances.0.CcnId ccn-025qoqpx \
    --Instances.0.UserAccountID 3436874624 \
    --Instances.0.RegionFlowControlId fcr-1duimd7w
```

Output: 
```
{
    "Response": {
        "RequestId": "098a99f2-d82c-47d4-8532-9322a315c8b4"
    }
}
```

