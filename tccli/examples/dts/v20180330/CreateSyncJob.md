**Example 1: Creating a Disaster Recovery Syn Task**

After purchasing a disaster recovery instance for your master instance, you need to create a disaster recovery sync task first before proceeding to next steps.

Input: 

```
tccli dts CreateSyncJob --cli-unfold-argument  \
    --JobName testname\
    --SrcDatabaseType mysql\
    --SrcAccessType cdb\
    --DstDatabaseType mysql\
    --DstAccessType cdb\
    --SyncOption.SyncObject 1\
    --SrcInfo.Region ap-shanghai\
    --SrcInfo.InstanceId cdb-e28hhsjt\
    --DstInfo.Region ap-shanghai\
    --DstInfo.InstanceId cdb-mdgezf4d
```

Output: 
```
{
    "Response": {
        "JobId": "sync-blj8wnt1",
        "RequestId": "f26f7628-7dad-457d-993e-2f03f0ff518d"
    }
}
```

