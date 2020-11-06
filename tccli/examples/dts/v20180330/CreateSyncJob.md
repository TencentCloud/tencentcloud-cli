**Example 1: 创建灾备同步任务**

用户为主实例购买了灾备实例后，首先需要创建灾备同步任务，然后才能开始灾备同步的后续流程。

Input: 

```
tccli dts CreateSyncJob --cli-unfold-argument  \
    --JobName testname \
    --SrcDatabaseType mysql \
    --SrcAccessType cdb \
    --DstDatabaseType mysql \
    --DstAccessType cdb \
    --SyncOption.SyncObject 1 \
    --SrcInfo.Region ap-shanghai \
    --SrcInfo.InstanceId cdb-e28hhsjt \
    --DstInfo.Region ap-shanghai \
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

