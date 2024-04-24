**Example 1: 查询资源是否开启密码轮转**

查询资源是否开启密码轮转

Input: 

```
tccli cdb DescribeDbTknResource --cli-unfold-argument  \
    --UserResourceId cdb-7qmr5idl \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount ssmtest1 \
    --InstanceType mysql \
    --AccountHost %
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

