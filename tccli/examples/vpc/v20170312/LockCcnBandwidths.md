**Example 1: 封禁限速实例**

封禁限速实例

Input: 

```
tccli vpc LockCcnBandwidths --cli-unfold-argument  \
    --Instances.0.CcnId ccn-cdnjw6bv \
    --Instances.0.UserAccountID 3436874624 \
    --Instances.0.RegionFlowControlId fcr-1duimd7w
```

Output: 
```
{
    "Response": {
        "RequestId": "64fb0c22-3122-4a99-840e-19db26df5e04"
    }
}
```

