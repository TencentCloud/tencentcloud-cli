**Example 1: 修改风险中心风险状态**

修改风险中心风险状态

Input: 

```
tccli csip ModifyRiskCenterRiskStatus --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --RiskStatusKeys.0.Id fc41d3fb2 \
    --RiskStatusKeys.0.PublicIPDomain 172.*.0.** \
    --RiskStatusKeys.0.InstanceId ins-ari443 \
    --RiskStatusKeys.0.AppId 23583341 \
    --Status 1 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7cf2ba3d-87ad-4691-a374-fd92ec11d9c8"
    }
}
```

