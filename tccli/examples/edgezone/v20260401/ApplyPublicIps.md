**Example 1: 申请公网Ipv4**



Input: 

```
tccli edgezone ApplyPublicIps --cli-unfold-argument  \
    --NetworkInstanceId epn-dfghjkl \
    --Type ipv4 \
    --Count 1
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-021",
        "IpList": [
            "224.12.10.25"
        ]
    }
}
```

**Example 2: 申请公网Ipv6**



Input: 

```
tccli edgezone ApplyPublicIps --cli-unfold-argument  \
    --NetworkInstanceId epn-xxxxxxxx \
    --Type ipv6 \
    --Count 1
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-021",
        "IpList": [
            "2001:db8::1"
        ]
    }
}
```

