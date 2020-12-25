**Example 1: 获取接收客户端请求的节点类型**

对于冷热分离的集群，可以通过该接口获取到当前集群用于接收客户端请求的节点类型

Input: 

```
tccli es GetRequestTargetNodeTypes --cli-unfold-argument  \
    --InstanceId es-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "8fd57721-808b-4f21-8f6b-51bca79ff1xx",
        "TargetNodeTypes": [
            "hot",
            "warm"
        ]
    }
}
```

