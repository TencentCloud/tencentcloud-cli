**Example 1: 查询用户对应的资源大账号信息**

查询用户对应的资源大账号信息

Input: 

```
tccli lighthouse DescribeUserOriginAccount --cli-unfold-argument  \
    --UserAppId 12345678
```

Output: 
```
{
    "Response": {
        "OriginAppId": 118977311,
        "OriginUin": "100210924731",
        "AccountState": "NORMAL",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

