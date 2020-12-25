**Example 1: 获取用户互联网公网地址配额信息**



Input: 

```
tccli dc DescribeInternetAddressQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Ipv4BgpQuota": 256,
        "Ipv4OtherQuota": 4,
        "Ipv6PrefixLen": 56,
        "Ipv4BgpNum": 50,
        "Ipv4OtherNum": 4,
        "RequestId": "aac03e7b-3c91-4970-b2bc-c20f0c6bdd38"
    }
}
```

