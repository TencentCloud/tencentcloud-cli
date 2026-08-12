**Example 1: 使用集群ID和配置ID查询当前配置**



Input: 

```
tccli goosefs DescribeClusterNodeMountPointConfig --cli-unfold-argument  \
    --ClusterId clst-Rg6BbE1K \
    --ConfigId cosfs2-config-id-3ee70bd7-3244-4068-81ae-7dbee09235f6
```

Output: 
```
{
    "Response": {
        "ConfigInstance": {
            "ClusterId": "clst-Rg6BbE1K",
            "ConfigId": "cosfs2-config-id-3ee70bd7-3244-4068-81ae-7dbee09235f6",
            "ConfigItems": [
                {
                    "Key": "file-cache.cache-dir",
                    "Value": "/tmp/write/test-string-type-new"
                }
            ],
            "ConfigName": "cosfs2.yaml",
            "CreateTime": 1779336128,
            "Description": "测试中文回显",
            "MPCount": 0,
            "UpdateTime": 1779336128,
            "Version": 5
        },
        "RequestId": "95e4d44d-7805-4d70-b57f-73d3d9f6f97a"
    }
}
```

