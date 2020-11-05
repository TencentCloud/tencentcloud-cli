**Example 1: Creating an organization**



Input: 

```
tccli organization CreateOrganization --cli-unfold-argument  \
    --OrgType 1
```

Output: 
```
{
    "Response": {
        "OrgId": 123,
        "Nickname": "test",
        "Mail": "test@qq.com",
        "OrgType": 1,
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

