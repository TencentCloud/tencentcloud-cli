**Example 1: 添加集群存储选项**



Input: 

```
tccli thpc AddClusterStorageOption --cli-unfold-argument  \
    --ClusterId hpc-eq97tf4u \
    --StorageOption.CFSOptions.0.LocalPath /data/ \
    --StorageOption.CFSOptions.0.RemotePath 172.30.3.90:/ \
    --StorageOption.CFSOptions.0.Protocol NFS 4.0 \
    --StorageOption.CFSOptions.0.StorageType SD \
    --StorageOption.CFSOptions.1.LocalPath /tmp/ \
    --StorageOption.CFSOptions.1.RemotePath 172.30.2.180@tcp0:/4fe1839b/cfs \
    --StorageOption.CFSOptions.1.Protocol TURBO \
    --StorageOption.CFSOptions.1.StorageType TB
```

Output: 
```
{
    "Response": {
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

