**Example 1: 创建添加子域名 Zone 域解析时所需要的 TXT 记录值参数示例**

创建添加子域名 Zone 域解析时所需要的 TXT 记录值

Input: 

```
tccli dnspod CreateSubdomainValidateTXTValue --cli-unfold-argument  \
    --DomainZone sub.dnspod.cn
```

Output: 
```
{
    "Response": {
        "Domain": "dnspod.cn",
        "Subdomain": "dnspodcheck",
        "RecordType": "TXT",
        "Value": "xxxxxxxxxxxx",
        "RequestId": "xx"
    }
}
```

