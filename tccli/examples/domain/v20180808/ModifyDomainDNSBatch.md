**Example 1: 批量修改域名DNS信息**



Input: 

```
tccli domain ModifyDomainDNSBatch --cli-unfold-argument  \
    --Domains h101.tencent.com \
    --Dns f1g1ns2.dnspod.net f1g1ns2.dnspod.net
```

Output: 
```
{
    "Response": {
        "LogId": 54,
        "RequestId": "ac64c5c2-c0f0-11ea-ba13-080027f4585e"
    }
}
```

