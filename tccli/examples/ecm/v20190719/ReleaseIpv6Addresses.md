**Example 1: 释放IPv6地址**



Input: 

```
tccli ecm ReleaseIpv6Addresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-9c8zkfev \
    --EcmRegion ap-xian-ecm \
    --Ipv6Addresses.0.Address 3402:4e00:20:1202:0:8d01:ee9c:3e22
```

Output: 
```
{
    "Response": {
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234",
        "TaskId": 3082
    }
}
```

