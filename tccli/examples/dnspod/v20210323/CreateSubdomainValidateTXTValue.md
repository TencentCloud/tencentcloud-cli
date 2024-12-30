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
        "Value": "3D015C717021A7A639D53673DB781317",
        "RequestId": "9cd72e8f-0bce-4330-b7d1-dcc402839a0a"
    }
}
```

