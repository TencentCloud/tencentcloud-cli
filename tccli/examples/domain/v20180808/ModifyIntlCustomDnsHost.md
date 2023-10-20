**Example 1: 修改自定义DNS**



Input: 

```
tccli domain ModifyIntlCustomDnsHost --cli-unfold-argument  \
    --DomainId domain-222222q \
    --DnsName ns1 \
    --IpSet 26.36.56.66
```

Output: 
```
{
    "Response": {
        "LogId": 200,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459398"
    }
}
```

