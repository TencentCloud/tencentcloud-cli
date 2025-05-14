**Example 1: 创建自定义DNS Host任务**

创建自定义DNS Host任务

Input: 

```
tccli domain CreateCustomDnsHost --cli-unfold-argument  \
    --DomainId domain-dwwwwwwq \
    --DnsName ns1 \
    --IpSet 1.2.4.8
```

Output: 
```
{
    "Response": {
        "LogId": 6543,
        "RequestId": "d4fc5332-23a2-49bd-8cab-48cfe5963651"
    }
}
```

