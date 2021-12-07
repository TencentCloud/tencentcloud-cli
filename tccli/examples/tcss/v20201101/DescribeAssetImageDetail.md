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
        "BuildHistory": "file:c92c248239f8c7b9b3c067650954815f391b7bcb09023f984972c082ace2a8d0 in  ",
        "ContainerCnt": 0,
        "CreateTime": "2021-01-29T04:03:11Z",
        "HostCnt": 1,
        "ImageID": "sha256:1c19ee40bfafd313400cde57a50b38b16ed4751c6b62a64141f18629a0e9d430",
        "ImageName": "<none>:<none>",
        "IsTrustImage": true,
        "OsName": "alpine:v3.12",
        "RemainScanTime": 0,
        "RequestId": "1d1ca0b5-f2ca-40bb-8797-39132bdbf35e",
        "RiskCnt": 7,
        "ScanError": "",
        "ScanRiskError": "",
        "ScanRiskProgress": 100,
        "ScanStatus": "SCAN_ERR",
        "ScanTime": "2021-01-29T05:26:18.07Z",
        "ScanVirusError": " 失败",
        "ScanVirusProgress": 100,
        "ScanVulError": "",
        "ScanVulProgress": 100,
        "SensitiveInfoCnt": 0,
        "Size": 16159906,
        "Status": 3,
        "VirusCnt": 11,
        "VulCnt": 5,
        "IsAuthorized": 0
    }
}
```

