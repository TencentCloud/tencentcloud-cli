**Example 1: 创建加速地域**



Input: 

```
tccli ga2 CreateAccelerateAreas --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --AcceleratorAreas.0.AccelerateRegion ap-guangzhou \
    --AcceleratorAreas.0.Bandwidth 13
```

Output: 
```
{
    "Response": {
        "RequestId": "dfbf77c2-5852-4ae3-b44a-fa6a5fd98b23",
        "TaskId": "5d1c5e75-a83b-49b4-be26-5bb3d2a376e8"
    }
}
```

