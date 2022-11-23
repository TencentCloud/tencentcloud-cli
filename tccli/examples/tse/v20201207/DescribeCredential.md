**Example 1: 查看临时凭证**



Input: 

```
tccli tse DescribeCredential --cli-unfold-argument  \
    --TenancyKey 100000
```

Output: 
```
{
    "Response": {
        "SecretKey": "xx",
        "Token": "xx",
        "SecretID": "xx",
        "ExpiredTime": 0,
        "RequestId": "xx"
    }
}
```

