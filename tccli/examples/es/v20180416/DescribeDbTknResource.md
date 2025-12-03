**Example 1: 获取实例账号是否开启cam授权**



Input: 

```
tccli es DescribeDbTknResource --cli-unfold-argument  \
    --InstanceType es \
    --UserResourceId es-f90lqeug \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount test1 \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "EnabledRotate": true,
        "RequestId": "1dc0cfd8-674f-43c2-815a-0ae102e90cd0"
    }
}
```

