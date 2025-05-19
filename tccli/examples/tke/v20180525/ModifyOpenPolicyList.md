**Example 1: 批量修改策略开关**



Input: 

```
tccli tke ModifyOpenPolicyList --cli-unfold-argument  \
    --ClusterId cls-gzzr1v5t \
    --Category optional \
    --OpenPolicyInfoList.0.EnforcementAction dryrun \
    --OpenPolicyInfoList.0.Name block-namespace-deletion-rule \
    --OpenPolicyInfoList.0.Kind blocknamespacedeletion
```

Output: 
```
{
    "Response": {
        "RequestId": "807af656-9c9b-43b0-bf8a-d0218b624ec7"
    }
}
```

