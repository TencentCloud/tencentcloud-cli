**Example 1: 切换域名ipv6开关**



Input: 

```
tccli waf ModifyDomainIpv6Status --cli-unfold-argument  \
    --InstanceId waf_2kw60zgy0908e8j3 \
    --Domain randygz2.qcloudwaf.com \
    --DomainId 7d58ebf3db7e5f7e8f91eb017c6a7b31 \
    --Status 2
```

Output: 
```
{
    "Response": {
        "RequestId": "e73994cd-f205-4f64-9878-aff70d81655d",
        "Ipv6Status": 1
    }
}
```

