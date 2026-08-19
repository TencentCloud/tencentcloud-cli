**Example 1: 查询 Pod 关联容器列表**



Input: 

```
tccli csip DescribePodContainerList --cli-unfold-argument  \
    --PodUniqueID a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 \
    --Filter.Limit 10 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 100,
        "List": [
            {
                "AppID": 1300448058,
                "AssetId": "",
                "ContainerId": "container-abc123",
                "ContainerName": "nginx",
                "RunStatus": "RUNNING",
                "NodeId": "ins-x08b",
                "NodeType": "CVM",
                "PodUid": "pod-uid-001",
                "PodName": "nginx-pod",
                "ImageId": "sha256:abc",
                "ImageName": "nginx:latest"
            }
        ],
        "RequestId": "12345cef-0bf7-4020-a6e8-b1f1ae4de7e2"
    }
}
```

