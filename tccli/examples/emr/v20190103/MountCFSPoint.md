**Example 1: 集群挂载CFS**



Input: 

```
tccli emr MountCFSPoint --cli-unfold-argument  \
    --InstanceId emr-kpcccpd4 \
    --MountInfo.HostMountShareDir /1122/workspace \
    --MountInfo.CFSMountShareDir /data/wedata/share/1122 \
    --MountInfo.FsIp 10.0.1.114 \
    --MountInfo.FsId cfs-icxljejj \
    --MountInfo.ProjectId 1122
```

Output: 
```
{
    "Response": {
        "RequestId": "278fb14d-4fd6-44a5-b8a8-22a8c17bcb0c"
    }
}
```

