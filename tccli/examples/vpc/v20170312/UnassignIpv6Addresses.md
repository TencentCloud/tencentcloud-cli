**Example 1: 释放IPv6地址**

释放IPv6地址

Input: 

```
tccli vpc UnassignIpv6Addresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-9c8zkfev \
    --Ipv6Addresses.0.Address 3402:4e00:20:1202:0:8d01:ee9c:3e22 \
    --Ipv6Addresses.1.Address 3402:4e00:20:1202:0:8d01:ee9c:3f7d \
    --Ipv6Addresses.2.Address 3402:4e00:20:1202:0:8d01:fef4:c7d5 \
    --Ipv6Addresses.3.Address 3402:4e00:20:1202:0:8d01:fef4:c97f
```

Output: 
```
{
    "Response": {
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234"
    }
}
```

