**Example 1: 在某集群内新建一个配置，指定配置名称和配置详情。**



Input: 

```
tccli goosefs CreateClusterNodeMountPointConfig --cli-unfold-argument  \
    --ClusterId clst-riQxF21P \
    --ConfigName cosfs2.yaml \
    --Description 测试中文回显 \
    --ConfigItems.0.Key file-system.temp-dir \
    --ConfigItems.0.Value "/tmp/write/dir/"
```

Output: 
```
{
    "Response": {
        "ConfigInstance": {
            "ClusterId": "clst-riQxF21P",
            "ConfigId": "cosfs2-config-id-89848918-ccbf-466f-8861-e6afeae3c819",
            "ConfigItems": [
                {
                    "Key": "file-system.temp-dir",
                    "Value": "/tmp/write/dir/"
                }
            ],
            "ConfigName": "cosfs2.yaml",
            "CreateTime": 1779355099,
            "Description": "测试中文回显",
            "MPCount": 0,
            "UpdateTime": 1779355099,
            "Version": 1
        },
        "RequestId": "2764f5d5-4d3a-47e3-9a52-b5de173a65f3"
    }
}
```

