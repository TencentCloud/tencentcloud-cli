**Example 1: 删除**

删除

Input: 

```
tccli tchousex DeleteAutoScalePlan --cli-unfold-argument  \
    --AutoScalePlan.Component clickhouse-server \
    --AutoScalePlan.InstanceID clickhouse-cn-7snrmiqf \
    --AutoScalePlan.VirtualCluster test01 \
    --InstanceId clickhouse-cn-7snrmiqf
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "b8bb3290-04c0-4b03-aea7-df0d6516a3d1"
    }
}
```

