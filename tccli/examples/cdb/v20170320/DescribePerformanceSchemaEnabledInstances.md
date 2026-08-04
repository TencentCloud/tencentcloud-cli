**Example 1: 查询指定实例中已开启PFS功能的信息**

当前指定实例未开启PFS功能

Input: 

```
tccli cdb DescribePerformanceSchemaEnabledInstances --cli-unfold-argument  \
    --InstanceIds cdb-qyew35pd
```

Output: 
```
{
    "Response": {
        "Items": [],
        "RequestId": "9e40f7f4-ce7a-4376-94ed-52e113359d97"
    }
}
```

