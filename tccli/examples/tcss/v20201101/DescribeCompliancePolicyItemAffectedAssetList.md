**Example 1: 查询检测项影响的资产列表**



Input: 

```
tccli tcss DescribeCompliancePolicyItemAffectedAssetList --cli-unfold-argument  \
    --CustomerPolicyItemId 45675 \
    --Offset 1000 \
    --Limit 10 \
    --Filters.0.Name NodeName \
    --Filters.0.Values node-1 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "AffectedAssetList": [
            {
                "AssetName": "hyperkube",
                "AssetType": "ASSET_IMAGE",
                "CheckResult": "RESULT_FAILED",
                "CheckStatus": "CHECK_FINISHED",
                "ClusterID": "cls-5licssbi",
                "ClusterName": "piper-容器告警接入安全中心测试",
                "CustomerAssetId": 1001005017196,
                "HostIP": "172.17.1.53",
                "ImageRegistryInfo": {
                    "Address": "",
                    "Name": "",
                    "Type": ""
                },
                "ImageTag": "v1.22.5-tke.27-rc1",
                "InstanceId": "ins-4bi3i496",
                "LastCheckTime": "2024-10-29 02:02:18",
                "NodeName": "as-tke-np-7lmwo8pi",
                "VerifyInfo": "sha256:f5b7776211ac931c484d203db03ed67e8b2dd44e0697119d02796a7d50041bcf:User="
            }
        ],
        "RequestId": "dce87f72-d7ad-4ed4-8cd4-688a8464aad3",
        "TotalCount": 186
    }
}
```

