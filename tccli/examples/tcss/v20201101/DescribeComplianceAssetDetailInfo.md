**Example 1: 请求资产详细信息**

请求资产详细信息

Input: 

```
tccli tcss DescribeComplianceAssetDetailInfo --cli-unfold-argument  \
    --CustomerAssetId 2202462 \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "AssetDetailInfo": {
            "AssetCreateTime": "2024-07-24 11:32:45",
            "AssetName": "my-elasticsearch-container",
            "AssetStatus": "ASSET_STOPPED",
            "AssetType": "ASSET_CONTAINER",
            "CheckResult": "RESULT_FAILED",
            "CheckStatus": "CHECK_FINISHED",
            "CustomerAssetId": 2202462,
            "FailedPolicyItemCount": 7,
            "HostIP": "172.16.49.104",
            "HostName": "VM-49-104-centos",
            "LastCheckTime": "2024-07-24 11:17:15",
            "NodeName": "云镜漏洞测试机-目标机器",
            "PassedPolicyItemCount": 17
        },
        "ContainerDetailInfo": {
            "ContainerId": "e822238a07e0",
            "PodName": ""
        },
        "HostDetailInfo": {
            "ContainerdVersion": "",
            "DockerVersion": "",
            "K8SVersion": ""
        },
        "ImageDetailInfo": {
            "ImageId": "",
            "ImageName": "",
            "ImageTag": "",
            "Repository": ""
        },
        "K8SDetailInfo": {
            "ClusterName": "",
            "ClusterVersion": ""
        },
        "RequestId": "ae46673b-3930-4874-9144-a514653d232c"
    }
}
```

