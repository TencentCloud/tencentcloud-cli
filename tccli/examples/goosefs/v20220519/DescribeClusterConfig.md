**Example 1: 创建集群配置**

创建集群配置

Input: 

```
tccli goosefs DescribeClusterConfig --cli-unfold-argument  \
    --ClusterId x_c60_r3c4fa1f \
    --ConfigFilename goosefs-site.properties
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6",
        "ConfigContent": "a2V5PXZhbHVl"
    }
}
```

