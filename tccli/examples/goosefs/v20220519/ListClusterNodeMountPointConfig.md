**Example 1: 指定MountPoint集群ID，返回结果按配置ID排序，返回第一页的配置列表，且最多返回100项**



Input: 

```
tccli goosefs ListClusterNodeMountPointConfig --cli-unfold-argument  \
    --ClusterId clst-a1uM4Bry  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "ConfigAbstractList": [
            {
                "ClusterId": "clst-a1uM4Bry",
                "ConfigId": "cosfs2-cfg-1f7178ba-1c30",
                "ConfigName": "test-config",
                "CreateTime": 1784709541,
                "Description": "test-create-config",
                "MPCount": 0,
                "UpdateTime": 1784709541,
                "Version": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "4be0f714-1f78-411a-b67d-7d0cb9ea7170"
    }
}
```

