**Example 1: 批量导出域名解析量参数示例**

批量导出域名解析量

Input: 

```
tccli dnspod CreateDomainsAnalyticsFile --cli-unfold-argument  \
    --Domains dnspod.cn \
    --DNSFormat DATE \
    --StartDate 2023-02-09 \
    --EndDate 2023-02-10
```

Output: 
```
{
    "Response": {
        "JobId": 1,
        "RequestId": "033a322d-e4e1-4b4d-bb74-aab903901d2f"
    }
}
```

