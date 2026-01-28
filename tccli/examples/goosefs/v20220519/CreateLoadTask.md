**Example 1: 创建预热任务**



Input: 

```
tccli goosefs CreateLoadTask --cli-unfold-argument  \
    --ClusterId g_cvm_hi052k4l \
    --LoadTaskCreationAttrs.TaskType DistributedLoad \
    --LoadTaskCreationAttrs.Priority 666 \
    --LoadTaskCreationAttrs.MetadataLoadAttrs.LoadType LoadByPath \
    --LoadTaskCreationAttrs.MetadataLoadAttrs.SkipIfExists False \
    --LoadTaskCreationAttrs.MetadataLoadAttrs.LoadByPath /goosefs_path/ \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.LoadType LoadByPath \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.LoadByPath /goosefs_path/ \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.Replica SingleReplica
```

Output: 
```
{
    "Response": {
        "TaskId": "baae4888-62e5-4027-bd56-070e82b2a584",
        "RequestId": "0174dedd-9c61-47aa-9ee9-1c5f901f8262"
    }
}
```

