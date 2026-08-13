**Example 1: 查询**



Input: 

```
tccli csip ModifyReverseShellSystemPolicyConfig --cli-unfold-argument  \
    --MemberId mem-tencent-b624e485fee5fe29 \
    --InnerNetAlarmShow True \
    --InnerIPShow True \
    --CWPScope 0 \
    --InstanceIDsWithAppId.0.AppId 260200475 \
    --InstanceIDsWithAppId.0.InstanceID ins-q4pf14qs \
    --ExcludeInstanceIDsWithAppId.0.AppId 260200475 \
    --ExcludeInstanceIDsWithAppId.0.InstanceID ins-q4pf14qs
```

Output: 
```
{
    "Response": {
        "RequestId": "d47b4a30-2082-4721-8843-594e0ce89108"
    }
}
```

