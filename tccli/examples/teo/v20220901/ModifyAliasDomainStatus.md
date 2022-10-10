**Example 1: 修改别称域名状态**



Input: 

```
tccli teo ModifyAliasDomainStatus --cli-unfold-argument  \
    --Paused True \
    --Filters.0.Values eo.example.com \
    --Filters.0.Name alias-name \
    --ZoneId zone-28569s6od5na
```

Output: 
```
{
    "Response": {
        "RequestId": "114327ee-463c-4ee4-83f6-82e9a44bd81d"
    }
}
```

