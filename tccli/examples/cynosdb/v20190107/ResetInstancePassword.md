**Example 1: 设置数据库账号密码**

设置数据库账号密码

Input: 

```
tccli cynosdb ResetInstancePassword --cli-unfold-argument  \
    --UserResourceId cynosdbysql-on5xw0ni \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount test \
    --AccountHost % \
    --Password sadaw@1
```

Output: 
```
{
    "Response": {
        "TimeCost": 250,
        "ResetTimestamp": 123145566,
        "RequestId": "abc"
    }
}
```

