**Example 1: 批量导出子域名解析量参数示例**

批量导出子域名解析量

Input: 

```
tccli dnspod CreateSubDomainsAnalyticsFile --cli-unfold-argument  \
    --Domains.0.Domain dnspod.cn \
    --Domains.0.SubDomain www \
    --Domains.0.Offset 0 \
    --Domains.0.Limit 1 \
    --DNSFormat DATE \
    --StartDate 2023-02-09 \
    --EndDate 2023-02-10 \
    --SubDomainType 1
```

Output: 
```
{
    "Response": {
        "JobId": 1,
        "RequestId": "85e43382-1c33-464b-b779-524461c79bd1"
    }
}
```

