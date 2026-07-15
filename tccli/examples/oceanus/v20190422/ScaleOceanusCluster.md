**Example 1: 扩容集群**

扩容Oceanus集群到19CU

Input: 

```
tccli oceanus ScaleOceanusCluster --cli-unfold-argument  \
    --ClusterId cluster-******** \
    --NewCU 19 \
    --ScaleMode ScaleUp
```

Output: 
```
{
    "Response": {
        "TaskExecResult": "success",
        "RequestId": "13a2d492-63d2-4d66-9ae1-e3e880999bfd"
    }
}
```

**Example 2: 缩容集群**

缩容Oceanus集群到12CU

Input: 

```
tccli oceanus ScaleOceanusCluster --cli-unfold-argument  \
    --ClusterId cluster-******** \
    --NewCU 12 \
    --ScaleMode ScaleDown
```

Output: 
```
{
    "Response": {
        "TaskExecResult": "success",
        "RequestId": "7e4577b4-42c0-4d1f-83a2-c0fd6fa0397e"
    }
}
```

