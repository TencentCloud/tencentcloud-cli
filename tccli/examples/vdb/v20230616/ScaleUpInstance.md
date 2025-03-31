**Example 1: 升配节点规格**

垂直扩容，升级指定实例的节点规格

Input: 

```
tccli vdb ScaleUpInstance --cli-unfold-argument  \
    --Cpu 4 \
    --Memory 8 \
    --InstanceId vdb-jnaj**** \
    --StorageSize 40
```

Output: 
```
{
    "Response": {
        "RequestId": "3b9204cd-6946-4688-8489-5707960ff6d3"
    }
}
```

