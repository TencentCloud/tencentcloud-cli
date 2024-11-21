**Example 1: 查询镜像详细信息**

查询镜像详细信息

Input: 

```
tccli tcss DescribeAssetImageDetail --cli-unfold-argument  \
    --ImageID dskaldjskld
```

Output: 
```
{
    "Response": {
        "AgentError": "",
        "Architecture": "",
        "Author": "",
        "BuildHistory": "# create_time:2021-09-15 18:20:05 tags:docker.io/centos:latest,yancyw:1,yancyw:2,yancyw:3, ADD file:1114113413411342942e068863ce2a8491bb71522c652f31fb466 in / ",
        "ContainerCnt": 51,
        "CreateTime": "2021-09-16 02:20:05",
        "HostCnt": 24,
        "ImageDigest": "sha256:113411341134134ab9dfb7c8571c40d67d534bbdee55bd6c473f432b177",
        "ImageID": "sha256:13413413413494c8a1ad043720b0416bfc16c52c45d4847e53fadb6",
        "ImageName": "docker.io/centos:latest",
        "IsAuthorized": 1,
        "IsTrustImage": true,
        "OsName": "centos:8.4.2105",
        "RemainScanTime": 0,
        "RequestId": "113411341134-1037-46b4-a9fc-b17f3a8f0b03",
        "RiskCnt": 211,
        "ScanError": "",
        "ScanRiskError": "",
        "ScanRiskProgress": 0,
        "ScanStatus": "",
        "ScanTime": "2024-10-25 16:13:39",
        "ScanVirusError": "",
        "ScanVirusProgress": 0,
        "ScanVulError": "",
        "ScanVulProgress": 0,
        "SensitiveInfoCnt": 0,
        "Size": 231268856,
        "Status": 5,
        "VirusCnt": 0,
        "VulCnt": 230
    }
}
```

