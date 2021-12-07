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
        "List": [
            {
                "Path": "/root/specimen_56d9739c7ecdbffa0f2f21efb33189fe",
                "RiskLevel": 4,
                "VirusName": "Script.VB.Ramnit.aa",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "Size": 342181,
                "FirstScanTime": "2021-01-15T09:14:46Z",
                "LatestScanTime": "2021-01-29T04:37:05.146Z",
                "Md5": "56d9739c7ecdbffa0f2f21efb33189fe",
                "FileName": ""
            }
        ],
        "RequestId": "8ca5c2e3-fb80-4e44-82f1-f561ef2b4ccf",
        "TotalCount": 11,
        "VirusScanStatus": 0
    }
}
```

