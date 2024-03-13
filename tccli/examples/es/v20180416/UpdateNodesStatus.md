**Example 1: 更新集群节点运行状态**

用于节点开机和关机

Input: 

```
tccli es UpdateNodesStatus --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --ActionType START \
    --NodeNames 159229897700074xxxx
```

Output: 
```
{
    "Response": {
        "FlowId": "33704",
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

