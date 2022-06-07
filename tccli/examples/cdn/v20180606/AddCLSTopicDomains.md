**Example 1: 新增日志主题下绑定的域名**



Input: 

```
tccli cdn AddCLSTopicDomains --cli-unfold-argument  \
    --LogsetId 6d04373b-ba59-4a4f-a96e-9fe53b59a536 \
    --TopicId d2256449-c6ff-421b-93ef-aa3a7dde2de2 \
    --DomainAreaConfigs.0.Domain a.b.com \
    --DomainAreaConfigs.0.Area mainland overseas
```

Output: 
```
{
    "Response": {
        "RequestId": "57460798-8723-45e3-9c75-a0599ef9143a"
    }
}
```

