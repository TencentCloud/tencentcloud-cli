**Example 1: 成功示例**



Input: 

```
tccli tione DescribeMountInstances --cli-unfold-argument  \
    --Type Cfs \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "MountInstances": [
            {
                "ExtraConf": {
                    "CFSProtocol": "NFS",
                    "CFSStorageType": "SD"
                },
                "Status": 0,
                "StorageId": "cfs-du6hjitx",
                "StorageName": "haroldyan",
                "Type": "Cfs"
            },
            {
                "ExtraConf": {
                    "CFSProtocol": "NFS",
                    "CFSStorageType": "SD"
                },
                "Status": 0,
                "StorageId": "cfs-cavy2v1x",
                "StorageName": "zoey-cfs",
                "Type": "Cfs"
            },
            {
                "ExtraConf": {
                    "CFSProtocol": "NFS",
                    "CFSStorageType": "SD"
                },
                "Status": 0,
                "StorageId": "cfs-fktuhiez",
                "StorageName": "bradyxie-cfs",
                "Type": "Cfs"
            },
            {
                "ExtraConf": {
                    "CFSProtocol": "TURBO",
                    "CFSStorageType": "TB"
                },
                "Status": 0,
                "StorageId": "cfs-47c3b0f37",
                "StorageName": "phye-ut-0",
                "Type": "Cfs"
            },
            {
                "ExtraConf": {
                    "CFSProtocol": "NFS",
                    "CFSStorageType": "SD"
                },
                "Status": 0,
                "StorageId": "cfs-f11afilz",
                "StorageName": "felixszheng_cfs",
                "Type": "Cfs"
            }
        ],
        "RequestId": "49c7d53e-5f8f-4dd9-8076-1c922308060b",
        "TotalCount": 28
    }
}
```

