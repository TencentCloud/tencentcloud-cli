**Example 1: 查询镜像列表**

查询镜像列表

Input: 

```
tccli tcss DescribeAssetImageList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ImageID": "sha256:2061084bfcc0d9ff44f479efc582e3ac9feaf96b556f6901bb39dbddfb9676b2",
                "ImageName": "l10:latest",
                "CreateTime": "2021-01-29T04:03:18Z",
                "Size": 16159906,
                "HostCnt": 12,
                "ContainerCnt": 0,
                "ScanTime": "2021-01-29T06:10:12.021Z",
                "VulCnt": 5,
                "ComponentCnt": 31,
                "VirusCnt": 141,
                "RiskCnt": 7,
                "IsTrustImage": true,
                "OsName": "alpine:v3.12",
                "AgentError": "No Error",
                "ScanError": "No Error",
                "ScanStatus": "SCANNED",
                "ScanVirusError": "No Error",
                "ScanVulError": "No Error",
                "ScanRiskError": "No Error",
                "IsSuggest": 0,
                "IsAuthorized": 12
            }
        ],
        "RequestId": "9c2d0eee-b4b8-4954-98ab-be69f503f77d",
        "TotalCount": 339
    }
}
```

