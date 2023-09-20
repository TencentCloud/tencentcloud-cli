**Example 1: 切换域名ipv6开关**



Input: 

```
tccli waf ModifyDomainIpv6Status --cli-unfold-argument  \
    --InstanceId waf_xxx \
    --Status 1 \
    --Domain waf_xxx \
    --DomainId waf_xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "Ipv6Status": 1
    }
}
```

