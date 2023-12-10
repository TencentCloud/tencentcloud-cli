**Example 1: 示例1**

查询是否支持就近接入

Input: 

```
tccli redis DescribeInstanceSupportFeature --cli-unfold-argument  \
    --InstanceId crs-fhsw2mh4 \
    --FeatureName read-local-node-only
```

Output: 
```
{
    "Response": {
        "RequestId": "60b6c537-1021-4360-a7b9-90feaca647a1",
        "Support": true
    }
}
```

