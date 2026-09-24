**Example 1: case 1**



Input: 

```
tccli ioa DescribeDeviceSecurityInfo --cli-unfold-argument  \
    --Mid D1098D67B85C540A2595BDF296953EDB6A89750F
```

Output: 
```
{
    "Response": {
        "Data": {
            "FirewallStatus": 1,
            "RealTimeProtectionStatus": 2,
            "SysRepVersion": "2026.07.31.11.45.06",
            "VirusVer": "2.0.13789.1131",
            "VulVersion": "2019.08.19.09.50.30"
        },
        "RequestId": "2ec430e1-1695-4db1-933a-a6765f8e66ae"
    }
}
```

