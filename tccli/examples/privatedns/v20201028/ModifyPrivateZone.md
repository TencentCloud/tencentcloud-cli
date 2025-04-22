**Example 1: 修改私有域**



Input: 

```
tccli privatedns ModifyPrivateZone --cli-unfold-argument  \
    --ZoneId zone-h91hca6u \
    --Remark 测试域名 \
    --DnsForwardStatus ENABLED \
    --CnameSpeedupStatus ENABLED
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845"
    }
}
```

