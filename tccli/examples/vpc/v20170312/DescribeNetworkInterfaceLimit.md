**Example 1: 根据CVM实例ID查询弹性网卡配额**

根据CVM实例ID查询弹性网卡配额

Input: 

```
tccli vpc DescribeNetworkInterfaceLimit --cli-unfold-argument  \
    --InstanceId ins-1991090i
```

Output: 
```
{
    "Response": {
        "EniPrivateIpAddressQuantity": 10,
        "ExtendEniPrivateIpAddressQuantity": 20,
        "ExtendEniQuantity": 0,
        "RequestId": "01f14f34-e9ae-470d-a71b-e8616ad3fae1",
        "EniQuantity": 2,
        "SubEniQuantity": 0,
        "SubEniPrivateIpAddressQuantity": 0
    }
}
```

**Example 2: 根据弹性网卡ID查询弹性网卡配额**

根据弹性网卡ID查询弹性网卡配额

Input: 

```
tccli vpc DescribeNetworkInterfaceLimit --cli-unfold-argument  \
    --InstanceId eni-1991090i
```

Output: 
```
{
    "Response": {
        "EniQuantity": 0,
        "EniPrivateIpAddressQuantity": 10,
        "ExtendEniQuantity": 0,
        "ExtendEniPrivateIpAddressQuantity": 0,
        "RequestId": "01f14f34-e9ae-470d-a71b-e8616ad3fae1",
        "SubEniQuantity": 0,
        "SubEniPrivateIpAddressQuantity": 0
    }
}
```

