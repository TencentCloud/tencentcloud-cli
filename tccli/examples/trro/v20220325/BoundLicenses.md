**Example 1: 绑定license**

为推流设备绑定license，优先绑定到期时间最近的，到期时间相同优先绑定月包

Input: 

```
tccli trro BoundLicenses --cli-unfold-argument  \
    --DeviceId remote11 \
    --ProjectId m82k54kco5arav1n \
    --Count 2
```

Output: 
```
{
    "Response": {
        "RequestId": "468bf31b-b5f7-44c4-8663-8d9548693cf5"
    }
}
```

