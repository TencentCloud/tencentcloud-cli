**Example 1: 续费包年包月实例**



Input: 

```
tccli mongodb RenewDBInstances --cli-unfold-argument  \
    --InstanceIds cmgo-gzo03o75 \
    --InstanceChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b1886334-acfe-4445-8429-e11a6e7b3851"
    }
}
```

