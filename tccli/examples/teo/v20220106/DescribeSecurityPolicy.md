**Example 1: 查询安全防护配置**



Input: 

```
tccli teo DescribeSecurityPolicy --cli-unfold-argument  \
    --Entity www.example.com \
    --ZoneId zone-xxqr76cy
```

Output: 
```
{
    "Response": {
        "AppId": 123456,
        "Config": null,
        "Entity": "www.example.com",
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae23",
        "ZoneId": "zone-xxqr76cy"
    }
}
```

