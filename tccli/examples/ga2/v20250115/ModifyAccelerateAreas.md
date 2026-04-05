**Example 1: 修改加速地域**



Input: 

```
tccli ga2 ModifyAccelerateAreas --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --AcceleratorAreas.0.AccelerateRegion ap-guangzhou \
    --AcceleratorAreas.0.Bandwidth 14
```

Output: 
```
{
    "Response": {
        "RequestId": "d9febac8-ac1a-4caf-93d8-e15f5d51a2c1",
        "TaskId": "9cd20fe4-0557-430c-95df-b06800da12f9"
    }
}
```

