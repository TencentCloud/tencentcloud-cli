**Example 1: 创建别称域名**



Input: 

```
tccli teo CreateAliasDomain --cli-unfold-argument  \
    --TargetName aaa.example.com \
    --AliasName bbb.test.com \
    --CertType none \
    --ZoneId zone-28569s6od5na
```

Output: 
```
{
    "Response": {
        "RequestId": "4dcgtb24-7dc5-46s2-9q3e-95825d53dcs3a"
    }
}
```

