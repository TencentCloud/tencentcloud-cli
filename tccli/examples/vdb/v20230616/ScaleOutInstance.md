**Example 1: 增加节点数量**

水平扩容节点数量

Input: 

```
tccli vdb ScaleOutInstance --cli-unfold-argument  \
    --InstanceId vdb-jnaj**** \
    --ReplicaNum 3
```

Output: 
```
{
    "Response": {
        "RequestId": "4a1162e1-e631-44c2-9ad4-ba2cf9f2cddc"
    }
}
```

