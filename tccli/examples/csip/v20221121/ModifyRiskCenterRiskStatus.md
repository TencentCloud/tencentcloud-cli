**Example 1: 修改风险中心风险状态**

修改风险中心风险状态

Input: 

```
tccli csip ModifyRiskCenterRiskStatus --cli-unfold-argument  \
    --MemberId abc \
    --RiskStatusKeys.0.Id abc \
    --RiskStatusKeys.0.PublicIPDomain abc \
    --RiskStatusKeys.0.InstanceId abc \
    --RiskStatusKeys.0.AppId abc \
    --Status 1 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

