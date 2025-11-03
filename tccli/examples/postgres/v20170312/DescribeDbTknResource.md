**Example 1: SSM侧检验对应数据库账户的合法性**



Input: 

```
tccli postgres DescribeDbTknResource --cli-unfold-argument  \
    --UserResourceId postgres-6bwgamo3 \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount root \
    --InstanceType postgres
```

Output: 
```
{
    "Response": {
        "RequestId": "93705d62-b156-43db-b7d7-0e24715a4f1c",
        "EnabledRotate": true
    }
}
```

