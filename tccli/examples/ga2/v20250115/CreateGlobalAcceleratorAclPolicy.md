**Example 1: 创建访问控制策略**



Input: 

```
tccli ga2 CreateGlobalAcceleratorAclPolicy --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --DefaultAction ACCEPT
```

Output: 
```
{
    "Response": {
        "RequestId": "bf1720f3-10af-4680-9066-f8ad032ecb38",
        "TaskId": "ad7fb6c7-d9c8-4142-93ae-386009164c6a",
        "GlobalAcceleratorAclPolicyId": "sp-fkp17zpx"
    }
}
```

