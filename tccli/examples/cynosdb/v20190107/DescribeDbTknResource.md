**Example 1: 查询数据库账号**

查询数据库账号

Input: 

```
tccli cynosdb DescribeDbTknResource --cli-unfold-argument  \
    --UserResourceId cynosdbysql-on5xw0ni \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount test \
    --AccountHost % \
    --InstanceType cynosdb
```

Output: 
```
{
    "Response": {
        "EnabledRotate": true,
        "RequestId": "abc"
    }
}
```

