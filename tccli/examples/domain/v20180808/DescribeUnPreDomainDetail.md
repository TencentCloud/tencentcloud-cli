**Example 1: 查询预释放未预约域名详情接口**



Input: 

```
tccli domain DescribeUnPreDomainDetail --cli-unfold-argument  \
    --Domain **m.com
```

Output: 
```
{
    "Response": {
        "RequestId": "cd4379ce-0fb7-1234-bc2f-5a68df5bcd20",
        "Domain": "**m.com",
        "PreCount": 8,
        "RegTime": "2005-11-23 02:26:00",
        "DeleteTime": "2025-01-23 02:26:00",
        "ExpireTime": "2024-12-23 02:26:00",
        "Status": "ing",
        "CurrentPrice": 198,
        "AppointBondPrice": 90,
        "IsAppoint": false,
        "BusinessId": "***046",
        "IsDomainUser": false
    }
}
```

