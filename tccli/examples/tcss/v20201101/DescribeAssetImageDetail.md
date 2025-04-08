**Example 1: 查询镜像详细信息**

查询镜像详细信息

Input: 

```
tccli tcss DescribeAssetImageDetail --cli-unfold-argument  \
    --ImageID sha256:707540fd8a54ab3ebc086ecc96d2d6143fd92c1cac4d0b23353e1b7078b5937b
```

Output: 
```
{
    "Response": {
        "AgentError": "timeout",
        "Architecture": "Metadata",
        "Author": "symon",
        "BuildHistory": "# create_time:2021-09-15 18:20:05 tags:docker.io/centos:latest,yancyw:1,yancyw:2,yancyw:3, ADD file:1114113413411342942e068863ce2a8491bb71522c652f31fb466 in / ",
        "ContainerCnt": 51,
        "CreateTime": "2021-09-16 02:20:05",
        "HostCnt": 24,
        "SuperNodeCnt": 1,
        "ImageDigest": "sha256:707540fd8a54ab3ebc086ecc96d2d6143fd92c1cac4d0b23353e1b7078b5937b",
        "ImageID": "sha256:707540fd8a54ab3ebc086ecc96d2d6143fd92c1cac4d0b23353e1b7078b5937b",
        "ImageName": "docker.io/centos:latest",
        "IsAuthorized": 1,
        "IsTrustImage": true,
        "OsName": "centos:8.4.2105",
        "RemainScanTime": 0,
        "RequestId": "a11d268f-1601-4f63-9131-0382537b9e55",
        "RiskCnt": 211,
        "ScanError": "timeout",
        "ScanRiskError": "timeout",
        "ScanRiskProgress": 0,
        "ScanStatus": "SCANNED",
        "ScanTime": "2024-10-25 16:13:39",
        "ScanVirusError": "timeout",
        "ScanVirusProgress": 0,
        "ScanVulError": "timeout",
        "ScanVulProgress": 0,
        "SensitiveInfoCnt": 0,
        "Size": 231268856,
        "Status": 5,
        "VirusCnt": 0,
        "VulCnt": 230
    }
}
```

