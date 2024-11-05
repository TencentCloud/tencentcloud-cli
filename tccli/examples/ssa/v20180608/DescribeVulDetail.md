**Example 1: 获取漏洞列表-漏洞详情**



Input: 

```
tccli ssa DescribeVulDetail --cli-unfold-argument  \
    --UniqId 1445149556-100199-a7db49fc-d918-11e8-b7a1-5cb90191b1e0
```

Output: 
```
{
    "Response": {
        "Source": "source",
        "Cnnvd": "NVD-2003-**",
        "ImpactAsset": "1",
        "IsAssetDeleted": false,
        "Cvss": "6.8",
        "Status": 1,
        "UpdateTime": "2020-10-10 12:12:12",
        "Cnvd": "CNVD-2003-**",
        "SsaAssetCategory": 0,
        "Desc": "description info",
        "CvssScore": "6.8",
        "Name": "vul name",
        "VulType": 0,
        "Level": 2,
        "ImpactAssetName": "asset name",
        "VulUrl": "http://excample.com",
        "VulPath": "/usr/bin",
        "RequestId": "f9184c15-9721-456d-8ca0-4263967b5ead",
        "Cve": "CVE-2003",
        "ReleaseTime": "2020-10-10 12:12:12",
        "Repair": "repair info",
        "Reference": "reference info",
        "SubVulType": "1"
    }
}
```

