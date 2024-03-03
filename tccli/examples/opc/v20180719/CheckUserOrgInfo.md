**Example 1: 检查用户是否是私域用户**



Input: 

```
tccli opc CheckUserOrgInfo --cli-unfold-argument  \
    --OwnerUin 100035685964
```

Output: 
```
{
    "Response": {
        "OwnerUin": "100035685964",
        "JoinTime": "2023-09-19 18:46:57",
        "InCompanyWechatOrg": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

