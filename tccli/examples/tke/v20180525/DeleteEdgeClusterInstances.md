**Example 1: 删除边缘计算实例**

删除边缘集群计算节点

Input: 

```
tccli tke DeleteEdgeClusterInstances --cli-unfold-argument  \
    --ClusterId cls-1234abcd \
    --InstanceIds cvm-xgj3ca32
```

Output: 
```
{
    "Response": {
        "RequestId": "187c16d5-1f53-4e88-b684-077f0c7369b2"
    }
}
```

