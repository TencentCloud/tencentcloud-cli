**Example 1: 查询实例轮转状态**



Input: 

```
tccli ckafka DescribeRoleTokenResource --cli-unfold-argument  \
    --UserResourceId ckafka-*****r87 \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount ckafka-*****r87#**ler \
    --InstanceType ckafka \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "EnabledRotate": false,
        "RequestId": "b918268b-7624-4a8c-891f-a0a58eb0efb5"
    }
}
```

