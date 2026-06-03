**Example 1: 成功样例**



Input: 

```
tccli tcss DescribeAssetImageRegistryList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ComponentCnt": 123,
                "ContainerCnt": 1,
                "CriticalLevelVulCnt": 0,
                "CveStatus": "SCANNED",
                "HasNeedFixVul": false,
                "HighLevelVulCnt": 0,
                "Id": 110207177,
                "ImageCreateTime": "2026-03-31T21:04:17+08:00",
                "ImageDigest": "sha256:1b31fd41db6d4119c43d4ec03571859f4eabc206b8a77fc8fb7940ed9e7c457d",
                "ImageId": "sha256:f2de8ed54c7b02ee05e42abaa454978c76fb552a883877b37588ebb62f31e41a",
                "ImageName": "ollama",
                "ImageRepoAddress": "ccr.ccs.tencentyun.com/csip/ollama",
                "ImageSize": 3360774711,
                "ImageTag": "latest",
                "InstanceId": "",
                "InstanceName": "ccr-ap-bangkok",
                "IsAuthorized": 0,
                "IsLatestImage": true,
                "IsRunning": true,
                "IsTrustImage": false,
                "LowLevelVulCnt": 0,
                "MediumLevelVulCnt": 0,
                "Namespace": "csip",
                "OsName": "linux",
                "Progress": 100,
                "Reason": "连接失败",
                "RecommendedFix": false,
                "RegistryRegion": "ap-bangkok",
                "RegistryType": "ccr",
                "RiskCnt": 0,
                "RiskStatus": "SCANNED",
                "ScanRemainTime": 0,
                "ScanRiskError": "",
                "ScanRiskProgress": 100,
                "ScanStatus": "SCANNED",
                "ScanTime": "2026-05-09T05:48:06+08:00",
                "ScanVirusError": "ConnFailed",
                "ScanVirusProgress": 100,
                "ScanVulError": "",
                "ScanVulProgress": 100,
                "SensitiveInfoCnt": 0,
                "SentiveInfoCnt": 0,
                "Solution": "扫描节点与仓库连接失败，请到镜像仓库管理重新配置连接方式后重试",
                "VirusCnt": 0,
                "VirusStatus": "SCAN_ERR",
                "VulCnt": 0
            }
        ],
        "TotalCount": 2145,
        "RequestId": "0785bc94-dbd3-4d82-b236-add96cab1f88"
    }
}
```

