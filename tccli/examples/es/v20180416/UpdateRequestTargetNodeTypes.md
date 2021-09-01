**Example 1: 更新接收客户端请求的节点类型**

对于冷热分离的集群，在温节点节点规格比较小的情况下，可以把来自客户端的请求只发送到热节点上，只让热节点承担协调节点的功能。

Input: 

```
tccli es UpdateRequestTargetNodeTypes --cli-unfold-argument  \
    --InstanceId es-xxxxxx \
    --TargetNodeTypes hot
```

Output: 
```
{
    "Response": {
        "RequestId": "8fd57721-808b-4f21-8f6b-51bca79ff1xx"
    }
}
```

