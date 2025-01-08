**Example 1: 删除当前集群的节点规格配置**



Input: 

```
tccli emr DeleteNodeResourceConfig --cli-unfold-argument  \
    --InstanceId emr-da13dada \
    --ResourceType CORE \
    --ResourceConfigId 1 \
    --ResourceBaseType EMR
```

Output: 
```
{
    "Response": {
        "RequestId": "8c2ff02e-5f38-494a-8d2d-68a7dec6efcd"
    }
}
```

