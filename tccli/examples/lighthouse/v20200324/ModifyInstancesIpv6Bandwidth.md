**Example 1: 修改实例IPv6带宽**

修改实例IPv6带宽

Input: 

```
tccli lighthouse ModifyInstancesIpv6Bandwidth --cli-unfold-argument  \
    --InstanceIds lhins-abcd1234 \
    --Ipv6Bandwidth 2
```

Output: 
```
{
    "Response": {
        "RequestId": "232b2817-ec08-43f3-8d78-41b1bfb6082c"
    }
}
```

