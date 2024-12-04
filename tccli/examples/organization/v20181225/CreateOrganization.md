**Example 1: 创建企业组织**



Input: 

```
tccli organization CreateOrganization --cli-unfold-argument  \
    --OrgType 1
```

Output: 
```
{
    "Response": {
        "OrgId": 101,
        "Nickname": "host_name",
        "Mail": "23***.qq.com",
        "OrgType": 1,
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

