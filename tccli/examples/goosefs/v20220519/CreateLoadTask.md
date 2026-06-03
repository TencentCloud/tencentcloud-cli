**Example 1: 创建DistributedLoad预热任务**



Input: 

```
tccli goosefs CreateLoadTask --cli-unfold-argument  \
    --ClusterId g_cvm_x******* \
    --LoadTaskCreationAttrs.TaskType DistributedLoad \
    --LoadTaskCreationAttrs.Priority 111 \
    --LoadTaskCreationAttrs.Description LoadTaskTest \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.LoadType LoadByPath \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.LoadByPath / \
    --LoadTaskCreationAttrs.DistributedLoadAttrs.Replica SingleReplica
```

Output: 
```
{
    "Response": {
        "TaskId": "32d8680e-fcdb-****-a190-47c140389246",
        "RequestId": "7f1b61db-b822-48b2-9004-f5edda11217c"
    }
}
```

**Example 2: 创建MetadataLoad预热任务**



Input: 

```
tccli goosefs CreateLoadTask --cli-unfold-argument  \
    --ClusterId g_cvm_x******* \
    --LoadTaskCreationAttrs.TaskType MetadataLoad \
    --LoadTaskCreationAttrs.Priority 222 \
    --LoadTaskCreationAttrs.Description LoadTaskTest \
    --LoadTaskCreationAttrs.MetadataLoadAttrs.LoadType LoadByPath \
    --LoadTaskCreationAttrs.MetadataLoadAttrs.LoadByPath /goosefs_path/ \
    --LoadTaskCreationAttrs.ReportPath cos://******-bj-**********/
```

Output: 
```
{
    "Response": {
        "TaskId": "c637a3b7-5593-****-b9cc-d65cf0fe2bb2",
        "RequestId": "9a3845e3-dc68-468d-8d88-6ccc459e118d"
    }
}
```

