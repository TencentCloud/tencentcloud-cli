**Example 1: 查询镜像木马病毒列表**



Input: 

```
tccli csip DescribeImageVirusList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VirusList": [
            {
                "Category": "1",
                "FileMd5": "7d75cec50ce24e459d6f86364bb819fd",
                "FileName": "webshell.php",
                "FileSize": 40,
                "FileType": "BIN",
                "FirstDetectedTime": "2026-06-29T23:57:03+08:00",
                "ImageId": "681",
                "LatestDetectedTime": "2026-01-19T17:30:40+08:00",
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "Path": "/bin/webshell.php",
                "RiskLevel": "CRITICAL",
                "Tags": "BIN",
                "VirusName": "Php.Trojan.Php.Dnhl"
            }
        ],
        "RequestId": "fa3dff5d-34a8-4d8e-9bd4-ec81b838056f"
    }
}
```

