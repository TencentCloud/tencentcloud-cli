**Example 1: 查询某个资产的详情**



Input: 

```
tccli tcss DescribeComplianceAssetDetailInfo --cli-unfold-argument  \
    --CustomerAssetId 123456789
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "AssetDetailInfo": {
            "CustomerAssetId": 123456789,
            "AssetType": "ASSET_CONTAINDER",
            "AssetName": "happy-jekins",
            "HostIP": "xx",
            "HostName": "xx",
            "NodeName": "worker-node-1",
            "CheckStatus": "CHECK_FINISHED",
            "AssetCreateTime": "2021-03-31 00:00:00",
            "AssetStatus": "ASSET_NORMAL",
            "LastCheckTime": "2021-04-02 16:42:00",
            "PassedPolicyItemCount": 100,
            "FailedPolicyItemCount": 10,
            "CheckResult": "RESULT_PASSED"
        },
        "ContainerDetailInfo": {
            "ContainerId": "xxxx",
            "PodName": "happy-jekins"
        },
        "K8SDetailInfo": {
            "ClusterName": "xx"
        },
        "HostDetailInfo": {
            "DockerVersion": "xx",
            "K8SVersion": "xx"
        },
        "ImageDetailInfo": {
            "ImageTag": "xx",
            "ImageName": "xx",
            "Repository": "xx",
            "ImageId": "xx"
        }
    }
}
```

