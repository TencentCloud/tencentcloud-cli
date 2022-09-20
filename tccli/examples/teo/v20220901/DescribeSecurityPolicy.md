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
        "SecurityConfig": {
            "SwitchConfig": {
                "WebSwitch": "on"
            }
        },
        "RequestId": "wef982hjg0-334j39-348j3w"
    }
}
```

