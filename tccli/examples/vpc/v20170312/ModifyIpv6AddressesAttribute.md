**Example 1: 修改弹性网卡IPv6地址属性**

修改弹性网卡IPv6地址属性

Input: 

```
tccli vpc ModifyIpv6AddressesAttribute --cli-unfold-argument  \
    --NetworkInterfaceId eni-9c8zkfev \
    --Ipv6Addresses.0.Address 3402:4e00:20:1202::7 \
    --Ipv6Addresses.0.Description abc
```

Output: 
```
{
    "Response": {
        "RequestId": "57065a05-9d50-476b-9cd6-97b0ddf03766"
    }
}
```

