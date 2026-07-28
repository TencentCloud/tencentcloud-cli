**Example 1: 添加节点到集群**

将节点添加到DB Custom集群中

Input: 

```
tccli dbdc AddNodesToDBCustomCluster --cli-unfold-argument  \
    --ClusterId dbcc-sizxd0hi \
    --NodeIds dbcn-7d59rhi5 \
    --ImageId img-7rqxtnh9 \
    --LoginSettings.Password mimaTest@1234 \
    --HostName dbcustom.khaos.worker-{IP} \
    --HostNameType 1 \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "TaskId": 1495,
        "RequestId": "72c2aefd-3093-449c-9a28-5d52ce20217c"
    }
}
```

