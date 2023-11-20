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
        "ImageID": "abc",
        "ImageName": "abc",
        "CreateTime": "abc",
        "Size": 1,
        "HostCnt": 1,
        "ContainerCnt": 1,
        "ScanTime": "abc",
        "VulCnt": 1,
        "RiskCnt": 1,
        "SensitiveInfoCnt": 1,
        "IsTrustImage": true,
        "OsName": "abc",
        "AgentError": "abc",
        "ScanError": "abc",
        "Architecture": "abc",
        "Author": "abc",
        "BuildHistory": "abc",
        "ScanVirusProgress": 1,
        "ScanVulProgress": 1,
        "ScanRiskProgress": 1,
        "ScanVirusError": "abc",
        "ScanVulError": "abc",
        "ScanRiskError": "abc",
        "ScanStatus": "abc",
        "VirusCnt": 1,
        "Status": 1,
        "RemainScanTime": 1,
        "IsAuthorized": 0,
        "ImageDigest": "abc",
        "RequestId": "abc"
    }
}
```

