**Example 1: Queries the ENI quota by CVM instance ID**



Input: 

```
tccli vpc DescribeNetworkInterfaceLimit --cli-unfold-argument ```

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

**Example 2: Queries the ENI quota by ENI ID**



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

