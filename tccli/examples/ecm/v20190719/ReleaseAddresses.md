**Example 1: 释放弹性公网IP**



Input: 

```
tccli ecm ReleaseAddresses --cli-unfold-argument  \
    --AddressIds eip-11112222 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "TaskId": "123",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

