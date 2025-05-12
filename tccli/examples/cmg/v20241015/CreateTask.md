**Example 1: 创建迁移任务**

创建迁移任务

Input: 

```
tccli cmg CreateTask --cli-unfold-argument  \
    --ProductCode cfs-master \
    --SecretID AKID70y5CFGD1dxxxxxxxx \
    --SecretKey iGahfVEl5FFxxxxxxx \
    --CFSData.SourceFs.LocalFolder /data/cfs-538z50a9/src \
    --CFSData.SourceFs.SubFolder / \
    --CFSData.SourceFs.FileSystemType NFS \
    --CFSData.SourceFs.FileSystemID 0a4274847f \
    --CFSData.SourceFs.IP 0a4274847f-nws8.cn-hangzhou.nas.aliyuncs.com \
    --CFSData.SourceFs.MountID  \
    --CFSData.DestFs.LocalFolder /data/cfs-538z50a9/dest \
    --CFSData.DestFs.SubFolder / \
    --CFSData.DestFs.FileSystemType NFS \
    --CFSData.DestFs.FileSystemID cfs-538z50a9 \
    --CFSData.DestFs.IP 10.0.0.4 \
    --CFSData.DestFs.MountID mfvir3sm \
    --TaskMode 1 \
    --ClusterID cluster-7OQ1b0JS \
    --Cmd CfsMigrate
```

Output: 
```
{
    "Response": {
        "RequestId": "5f76ca39-1c0d-4a30-91b7-ab8d8c6d557e",
        "TaskID": "task-ZQqiMPrE"
    }
}
```

