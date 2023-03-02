**Example 1: 查询域名过期信息**

查询域名过期信息

Input: 

```
tccli domain DescribeDomainExpireInfo --cli-unfold-argument  \
    --Domain qcloud.xyz
```

Output: 
```
{
    "Response": {
        "Domain": "qcloud.xyz",
        "Registrar": "epp",
        "Expired": false,
        "ExpireTime": "2021-03-31 07:59:59",
        "RequestId": "9112984c-f4ee-4446-b70b-8eac6f44ca2e"
    }
}
```

