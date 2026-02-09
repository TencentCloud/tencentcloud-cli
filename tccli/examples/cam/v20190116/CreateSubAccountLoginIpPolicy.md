**Example 1: 增加子账号登录IP策略**



Input: 

```
tccli cam CreateSubAccountLoginIpPolicy --cli-unfold-argument  \
    --ApproverType SubAccountLoginLimitApproval \
    --IpPolicies.0.IP 192.168.1.171 \
    --IpPolicies.0.Effect Allow \
    --PolicyType 1 \
    --DisablePolicy 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9ad60b60-222f-4e22-8350-3227bebaa3dd"
    }
}
```

