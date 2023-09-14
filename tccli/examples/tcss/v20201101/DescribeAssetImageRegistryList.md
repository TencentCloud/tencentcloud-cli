**Example 1: 镜像仓库查询镜像仓库列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryList --cli-unfold-argument  \
    --Filters.0.ExactMatch False \
    --Filters.0.Name ScanStatus \
    --Filters.0.Values all \
    --Filters.1.ExactMatch False \
    --Filters.1.Name RepoType \
    --Filters.1.Values all \
    --Filters.2.ExactMatch False \
    --Filters.2.Name SecurityRisk \
    --Filters.2.Values all \
    --Filters.3.ExactMatch False \
    --Filters.3.Name IsAuthorized \
    --Filters.3.Values all \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a17ead82-00d3-4bf2-8ec2-55292c42d6e3",
        "TotalCount": 100,
        "List": [
            {
                "Id": 20933905,
                "ImageDigest": "sha256:8d8d7593f6da4e909bba63a3a22080eca935c57afd81ad0b8f069b90064324ba",
                "ImageId": "sha256:a810b384f08c95a472d7364b9b3198d4746f1ea001a26c5cb9d7e95272004afc",
                "RegistryType": "ccr",
                "RegistryRegion": "default",
                "ImageRepoAddress": "ccr.ccs.tencentyun.com/xcar/executor",
                "InstanceId": "",
                "InstanceName": "ccr-default",
                "Namespace": "xcar",
                "ImageName": "executor",
                "ImageTag": "latest",
                "ImageSize": 22952972,
                "ScanTime": "",
                "ScanStatus": "NOT_SCAN",
                "Progress": 0,
                "VulCnt": 0,
                "VirusCnt": 0,
                "RiskCnt": 0,
                "SentiveInfoCnt": 0,
                "IsTrustImage": false,
                "OsName": "linux",
                "ScanVirusError": "",
                "ScanVulError": "",
                "ScanRiskError": "",
                "ScanVirusProgress": 0,
                "ScanVulProgress": 0,
                "ScanRiskProgress": 0,
                "ScanRemainTime": 0,
                "CveStatus": "NOT_SCAN",
                "RiskStatus": "NOT_SCAN",
                "VirusStatus": "NOT_SCAN",
                "IsAuthorized": 0,
                "ImageCreateTime": "2020-09-22T00:00:00+00:00",
                "IsLatestImage": true
            },
            {
                "Id": 20933905,
                "ImageDigest": "sha256:8d8d7593f6da4e909bba63a3a22080eca935c57afd81ad0b8f069b90064324ba",
                "ImageId": "sha256:a810b384f08c95a472d7364b9b3198d4746f1ea001a26c5cb9d7e95272004afc",
                "RegistryType": "ccr",
                "RegistryRegion": "default",
                "ImageRepoAddress": "ccr.ccs.tencentyun.com/xcar/executor",
                "InstanceId": "",
                "InstanceName": "ccr-default",
                "Namespace": "xcar",
                "ImageName": "executor",
                "ImageTag": "latest",
                "ImageSize": 22952972,
                "ScanTime": "",
                "ScanStatus": "NOT_SCAN",
                "Progress": 0,
                "VulCnt": 0,
                "VirusCnt": 0,
                "RiskCnt": 0,
                "SentiveInfoCnt": 0,
                "IsTrustImage": false,
                "OsName": "linux",
                "ScanVirusError": "",
                "ScanVulError": "",
                "ScanRiskError": "",
                "ScanVirusProgress": 0,
                "ScanVulProgress": 0,
                "ScanRiskProgress": 0,
                "ScanRemainTime": 0,
                "CveStatus": "NOT_SCAN",
                "RiskStatus": "NOT_SCAN",
                "VirusStatus": "NOT_SCAN",
                "IsAuthorized": 0,
                "ImageCreateTime": "2020-09-22T00:00:00+00:00",
                "IsLatestImage": true
            }
        ]
    }
}
```

