**Example 1: 创建安全 IP 组**

正常创建安全 IP 组

Input: 

```
tccli teo CreateSecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 0 \
    --IPGroup.Name testip \
    --IPGroup.Content 2.2.2.2 \
    --ZoneId zone-j94jf0a1
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-xxxx-27cb34dac669",
        "GroupId": 128
    }
}
```

