**Example 1: 查询某类资产的列表**



Input: 

```
tccli tcss DescribeComplianceAssetList --cli-unfold-argument  \
    --AssetTypeSet ASSET_CONTAINDER \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AssetInfoList": [
            {
                "CustomerAssetId": 14343206,
                "AssetType": "ASSET_CONTAINER",
                "AssetName": "name-asset",
                "ImageTag": "latest",
                "HostIP": "172.16.0.1",
                "NodeName": "node-1",
                "CheckStatus": "CHECK_FINISHED",
                "PassedPolicyItemCount": 1,
                "FailedPolicyItemCount": 1,
                "LastCheckTime": "2020-09-22 00:00:00",
                "CheckResult": "RESULT_FAILED",
                "InstanceId": "ins-busi1",
                "ImageRegistryInfo": {
                    "Name": "registry1",
                    "Type": "habor",
                    "Address": "http://1.1.1.2"
                },
                "ClusterID": "cluster-busi1",
                "ClusterName": "cluster1"
            }
        ],
        "RequestId": "1e6c6a5d-740b-40f5-8685-47467df4df45"
    }
}
```

