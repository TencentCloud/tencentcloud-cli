**Example 1: 镜像仓库查询木马病毒列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryVirusList --cli-unfold-argument  \
    --Filters.0.ExactMatch False \
    --Filters.0.Name RiskLevel \
    --Filters.0.Values all \
    --Id 6947411 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "ae035bd6-6e5a-4f3e-b3ce-1f9cf6917066",
        "List": [
            {
                "Path": "var/cache/debconf/passwords.dat",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "passwords.dat",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "etc/.pwd.lock",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": ".pwd.lock",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/triggers/Unincorp",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "Unincorp",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/apt-daily.timer",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "apt-daily.timer",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/triggers/Lock",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "Lock",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/log/btmp",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "btmp",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/statoverride",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "statoverride",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/lock",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "lock",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/log/wtmp",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "wtmp",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "run/utmp",
                "RiskLevel": "4",
                "Category": "",
                "VirusName": "stargate.lock",
                "Tags": [],
                "Desc": "",
                "Solution": "",
                "FileType": "",
                "FileName": "utmp",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            }
        ],
        "TotalCount": 17
    }
}
```

