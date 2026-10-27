**Example 1: CreateCommandTask**



Input: 

```
tccli cvd CreateCommandTask --cli-unfold-argument  \
    --Command aXBjb25maWc= \
    --Type PowerShellScript \
    --RunAsBoundUser False \
    --RunForeground False \
    --InstanceIds cdi-i71kxu6t60auxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "CommandId": "ac5b1e88-9862-423e-9595-10f2998096b5"
    }
}
```

