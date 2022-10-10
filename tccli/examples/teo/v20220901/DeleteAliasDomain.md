**Example 1: 删除别称域名**



Input: 

```
tccli teo DeleteAliasDomain --cli-unfold-argument  \
    --ZoneId zone-28569s6od5na \
    --Filters.0.Values eo.example.com \
    --Filters.0.Name alias-name
```

Output: 
```
{
    "Response": {
        "RequestId": "28ec90d3-7af9-460c-bb1a-dd9cf4d8c785"
    }
}
```

