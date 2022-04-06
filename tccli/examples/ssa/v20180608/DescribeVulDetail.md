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
        "Source": "xx",
        "Cnnvd": "xx",
        "ImpactAsset": "xx",
        "IsAssetDeleted": false,
        "Cvss": "xx",
        "Status": 1,
        "UpdateTime": "xx",
        "Cnvd": "xx",
        "SsaAssetCategory": 0,
        "Desc": "xx",
        "CvssScore": "xx",
        "Name": "xx",
        "VulType": 0,
        "Level": 2,
        "ImpactAssetName": "xx",
        "VulUrl": "xx",
        "VulPath": "xx",
        "RequestId": "xx",
        "Cve": "xx",
        "ReleaseTime": "xx",
        "Repair": "xx",
        "Reference": "xx",
        "SubVulType": "xx"
    }
}
```

