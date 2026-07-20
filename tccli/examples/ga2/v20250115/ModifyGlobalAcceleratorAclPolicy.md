**Example 1: 修改访问控制策略状态**



Input: 

```
tccli ga2 ModifyGlobalAcceleratorAclPolicy --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --GlobalAcceleratorAclPolicyId sp-00000msz \
    --Status OPEN
```

Output: 
```
{
    "Response": {
        "RequestId": "3dc1fa6a-4603-4675-a806-9630cf64f7e0",
        "TaskId": "5d5f34f4-e6f1-40bc-8424-91a86601e9e4"
    }
}
```

