**Example 1: 创建实例**

创建hai实例

Input: 

```
tccli hai RunInstances --cli-unfold-argument  \
    --ApplicationId app-jknfna \
    --BundleType S \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 250 \
    --InstanceName test
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "hai-qcgdfaptd"
        ],
        "RequestId": "e267492d-fadaf-45a9-a139-416bc8652861"
    }
}
```

