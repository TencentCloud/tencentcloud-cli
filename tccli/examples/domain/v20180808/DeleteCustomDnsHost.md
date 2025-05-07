**Example 1: 创建删除自定义DNS Host任务**

创建删除自定义DNS Host任务

Input: 

```
tccli domain DeleteCustomDnsHost --cli-unfold-argument  \
    --DomainId domain-esydsfsdq \
    --DnsName ns1
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

