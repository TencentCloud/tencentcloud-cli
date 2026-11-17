**Example 1: 绑定自定义域名**



Input: 

```
tccli makers CreateZoneCustomDomain --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --Domain ************************ \
    --Env Production
```

Output: 
```
{
    "Response": {
        "Domain": "************************",
        "Id": "***************",
        "RequestId": "17e19340-013c-4451-aee2-b3f2cf48ab9d"
    }
}
```

