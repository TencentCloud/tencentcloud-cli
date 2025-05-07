**Example 1: 创建修改自定义DNS Host任务**

创建修改自定义DNS Host任务

Input: 

```
tccli domain ModifyCustomDnsHost --cli-unfold-argument  \
    --DomainId domain-esyfsdfgq \
    --DnsName ns1 \
    --IpSet 2.2.2.2 1.2.4.8
```

Output: 
```
{
    "Response": {
        "LogId": 510702,
        "RequestId": "d4fc5332-23a2-49bd-8cab-48cfe5963651"
    }
}
```

