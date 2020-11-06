**Example 1: 绑定EIP到实例上**

实例主网卡无外网IP条件下，将EIP绑定到实例主网卡

Input: 

```
tccli ecm AssociateAddress --cli-unfold-argument  \
    --AddressId eip-11112222 \
    --InstanceId ins-11221122 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "TaskId": "123",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

