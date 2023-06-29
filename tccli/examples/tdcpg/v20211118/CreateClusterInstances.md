**Example 1: 创建实例**



Input: 

```
tccli tdcpg CreateClusterInstances --cli-unfold-argument  \
    --InstanceCount 1 \
    --ClusterId tdcpg-xxx \
    --InstanceName MyInstanceName \
    --CPU 1 \
    --Memory 2
```

Output: 
```
{
    "Response": {
        "DealNameSet": [
            "20211028111234680033121"
        ],
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

