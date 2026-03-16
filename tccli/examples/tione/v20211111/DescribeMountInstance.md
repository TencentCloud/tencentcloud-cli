**Example 1: 成功示例**



Input: 

```
tccli tione DescribeMountInstance --cli-unfold-argument  \
    --Type Cfs \
    --StorageId cfs-du6hjitx
```

Output: 
```
{
    "Response": {
        "MountInstance": {
            "ExtraConf": {
                "CFSProtocol": "NFS",
                "CFSStorageType": "SD"
            },
            "Status": 0,
            "StorageId": "cfs-du6hjitx",
            "StorageName": "haroldyan",
            "Type": "Cfs"
        },
        "RequestId": "cadb6775-ccaf-4c65-8e03-42d1590a3eb3"
    }
}
```

