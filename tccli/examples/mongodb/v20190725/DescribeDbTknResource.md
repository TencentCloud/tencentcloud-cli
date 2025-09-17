**Example 1: 查询DBTkn资源信息**



Input: 

```
tccli mongodb DescribeDbTknResource --cli-unfold-argument  \
    --UserResourceId cmgo-abcdefg \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount readonly \
    --InstanceType mongodb
```

Output: 
```
{
    "Response": {
        "RequestId": "9ab09c94-b2fc-4053-9115-ccc178e56000",
        "EnabledRotate": true
    }
}
```

