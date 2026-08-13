**Example 1: 新建EDR策略**



Input: 

```
tccli csip ModifyEDRRule --cli-unfold-argument  \
    --RuleType 1 \
    --AlertAction 1 \
    --CWPScope 0 \
    --TCSSScope 0 \
    --Status 0 \
    --MemberId mem-tencent-e74488e0ba0cd8fe \
    --Name 容器白名单测试3 \
    --ContentType ip_outbound \
    --Description 都是 \
    --DealOldEvents 0 \
    --OutboundIP MS4xLjEuNw== \
    --ImageIDs 'sha256: 3599d4bcee082427c6b335a5b0d98892d2f5f0d7b1e5dc49c12e882f0f4a133f' \
    --TargetAppIDs 260199983 \
    --TagIDs tag1 \
    --ClusterIDsWithAppId.0.AppId 260199983 \
    --ClusterIDsWithAppId.0.ClusterID cls-ctra5rtk \
    --ExcludeClusterIDsWithAppId.0.AppId 260199983 \
    --ExcludeClusterIDsWithAppId.0.ClusterID cls-nac4o61q \
    --ImageIDsWithAppId.0.AppId 260199983 \
    --ImageIDsWithAppId.0.ImageID sha256:543c854dae852d401f6fe319e677d927050f2ca9fc5853e880bccef2cbb34c09 \
    --ConditionMatches.0.ImageAddressMatchString imageaddress \
    --ConditionMatches.0.MatchType CONTAINS
```

Output: 
```
{
    "Response": {
        "RequestId": "d5f769b8-abd9-47d0-82c2-6bb894331396"
    }
}
```

