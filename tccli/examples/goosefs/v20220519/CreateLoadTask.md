**Example 1: 创建预热任务**



Input: 

```
tccli goosefs CreateLoadTask --cli-unfold-argument  \
    --ClusterId g_cvm_******** \
    --LoadTaskCreationAttrs.TaskType DistributedLoad \
    --LoadTaskCreationAttrs.Priority 5454 \
    --LoadTaskCreationAttrs.Description sdasdasd \
    --LoadTaskCreationAttrs.MetadataLoadAttrs.LoadType LoadByPath \
    --LoadTaskCreationAttrs.MetadataLoadAttrs.LoadByPath / \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.LoadType LoadByList \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.LoadByList cos://**********-**-**********/test.txt \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.Replica SingleReplica
```

Output: 
```
{
    "Response": {
        "TaskId": "10dda4fd-a28e-4c43-b4cd-e2678571a078",
        "RequestId": "d457f4a3-34ba-4c49-a21a-7c5614796596"
    }
}
```

