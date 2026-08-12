**Example 1: 根据集群ID和配置ID，更新配置名称和配置描述，并全量覆盖配置详情。**



Input: 

```
tccli goosefs UpdateClusterNodeMountPointConfig --cli-unfold-argument  \
    --ClusterId clst-Rg6BbE1K \
    --ConfigId cosfs2-config-id-3ee70bd7-3244-4068-81ae-7dbee09235f6 \
    --NewConfigItems.0.Key cos.test.key \
    --NewConfigItems.0.Value cos.test.value1 \
    --NewConfigName cosfs2.yaml \
    --NewDescription 测试中文回显
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
                    "Key": "cos.test.key",
                    "Value": "cos.test.value1"
                }
            ],
            "ConfigName": "cosfs2.yaml",
            "CreateTime": 1779335847,
            "Description": "测试中文回显",
            "MPCount": 0,
            "UpdateTime": 1779335847,
            "Version": 3
        },
        "RequestId": "c48e4bf6-0780-4025-851f-fdd182658446"
    }
}
```

