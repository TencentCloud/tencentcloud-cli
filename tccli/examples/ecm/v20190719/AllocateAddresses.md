**Example 1: 创建EIP**



Input: 

```
tccli ecm AllocateAddresses --cli-unfold-argument  \
    --AddressCount 1 \
    --InternetServiceProvider CTCC \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            "eip-11112222"
        ],
        "TaskId": "123",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

