**Example 1: 批量创建私有域**



Input: 

```
tccli privatedns CreatePrivateZoneList --cli-unfold-argument  \
    --Domains 1.com 2.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845"
    }
}
```

