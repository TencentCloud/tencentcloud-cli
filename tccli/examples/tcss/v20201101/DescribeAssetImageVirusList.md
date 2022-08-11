**Example 1: 查询镜像病毒列表**

查询镜像病毒列表

Input: 

```
tccli tcss DescribeAssetImageVirusList --cli-unfold-argument  \
    --ImageID dskaldjskld
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "FirstScanTime": "xx",
                "Tags": [
                    "xx"
                ],
                "RiskLevel": 1,
                "VirusName": "xx",
                "Solution": "xx",
                "FileName": "xx",
                "Md5": "xx",
                "LatestScanTime": "xx",
                "Path": "xx",
                "Size": 1,
                "Desc": "xx",
                "CheckPlatform": [
                    "xx"
                ]
            }
        ],
        "RequestId": "xx",
        "VirusScanStatus": 1
    }
}
```

