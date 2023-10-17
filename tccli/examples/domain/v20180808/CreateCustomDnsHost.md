**Example 1: 创建自定义DNS Host任务**



Input: 

```
tccli domain CreateCustomDnsHost --cli-unfold-argument  \
    --DomainId domain-esfdhgfgdhigq \
    --DnsName ccc \
    --IpSet 8.8.9.9
```

Output: 
```
{
    "Response": {
        "LogId": 510694,
        "RequestId": "d4fc5332-23a2-49bd-8cab-48cfe5963651"
    }
}
```

