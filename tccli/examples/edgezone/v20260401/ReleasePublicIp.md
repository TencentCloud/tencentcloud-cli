**Example 1: 释放公网 Ipv4**



Input: 

```
tccli edgezone ReleasePublicIp --cli-unfold-argument  \
    --NetworkInstanceId epn-dfghjkl \
    --Type ipv4 \
    --IpList 226.10.12.3 226.10.12.4
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-026"
    }
}
```

**Example 2: 释放公网 Ipv6**



Input: 

```
tccli edgezone ReleasePublicIp --cli-unfold-argument  \
    --NetworkInstanceId epn-xxxxxxxx \
    --Type ipv6 \
    --IpList 2001:db8::1a2b 2001:db8::3c4d
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-026"
    }
}
```

