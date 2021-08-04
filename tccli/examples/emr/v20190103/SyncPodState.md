**Example 1: EMR同步Pod状态**



Input: 

```
tccli emr SyncPodState --cli-unfold-argument  \
    --Message.Name pod-1 \
    --Message.Reason pod is deleted \
    --Message.OwnerCluster emr-cluster \
    --Message.State POD_STATE_DELETED \
    --Message.Memory 0 \
    --Message.Uuid 3435346
```

Output: 
```
{
    "Response": {
        "RequestId": "d830face-6587-4263-8ab0-56bda265787d"
    }
}
```

