**Example 1: 获取关联某集群的实例列表**

获取关联某集群的实例列表

Input: 

```
tccli monitor DescribePrometheusAgentInstances --cli-unfold-argument  \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "Instances": [
            "prome-xxx"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

