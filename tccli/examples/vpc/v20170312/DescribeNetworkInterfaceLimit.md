**Example 1: 根据CVM实例ID查询弹性网卡配额**



Input: 

```
tccli vpc DescribeNetworkInterfaceLimit --cli-unfold-argument  \
    --InstanceId ins-1991090i
```

Output: 
```
{
    "Response": {
        "EniQuantity": 2,
        "EniPrivateIpAddressQuantity": 10,
        "RequestId": "01f14f34-e9ae-470d-a71b-e8616ad3fae1"
    }
}
```

**Example 2: 根据弹性网卡ID查询弹性网卡配额**



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
        "RequestId": "01f14f34-e9ae-470d-a71b-e8616ad3fae1"
    }
}
```

