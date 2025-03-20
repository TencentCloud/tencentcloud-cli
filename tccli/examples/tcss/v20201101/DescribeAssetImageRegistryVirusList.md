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
                "Category": "2",
                "VirusName": "stargate.lock",
                "Tags": [
                    "tag1"
                ],
                "Desc": "发现容器上存在恶意木马，您的容器可能已经失陷。\n恶意木马通常会执行挖矿、文件删除、信息窃取和网络攻击等恶****",
                "Solution": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；\n2.隔离或者删除相关的木马文件；\n3.对系统进行风险排查，并进行安全加固，详情可参考如下链接： \n【Linux】https://cloud.tencent.com/document/product/296/9604 \n【Windows】https://cloud.tencent.com/document/product/296/****",
                "FileType": "UNKOWN",
                "FileName": "passwords.dat",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "etc/.pwd.lock",
                "RiskLevel": "4",
                "Category": "2",
                "VirusName": "stargate.lock",
                "Tags": [
                    "tag2"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": ".pwd.lock",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/triggers/Unincorp",
                "RiskLevel": "4",
                "Category": "Category",
                "VirusName": "stargate.lock",
                "Tags": [
                    "2"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": "Unincorp",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/apt-daily.timer",
                "RiskLevel": "4",
                "Category": "Category",
                "VirusName": "stargate.lock",
                "Tags": [
                    "3"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": "apt-daily.timer",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/triggers/Lock",
                "RiskLevel": "4",
                "Category": "Category",
                "VirusName": "stargate.lock",
                "Tags": [
                    "3"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": "Lock",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/log/btmp",
                "RiskLevel": "4",
                "Category": "Category",
                "VirusName": "stargate.lock",
                "Tags": [
                    "5"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": "btmp",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/statoverride",
                "RiskLevel": "4",
                "Category": "Category",
                "VirusName": "stargate.lock",
                "Tags": [
                    "6"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": "statoverride",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/lib/dpkg/lock",
                "RiskLevel": "4",
                "Category": "Category",
                "VirusName": "stargate.lock",
                "Tags": [
                    "56"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": "lock",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "var/log/wtmp",
                "RiskLevel": "4",
                "Category": "6",
                "VirusName": "stargate.lock",
                "Tags": [
                    "tag1"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
                "FileName": "wtmp",
                "FileMd5": "d41d8cd98f00b204e9800998ecf8427e",
                "FileSize": 0,
                "FirstScanTime": "2021-01-30 03:31:56 +0000 UTC",
                "LatestScanTime": "2021-01-30 05:14:07 +0000 UTC"
            },
            {
                "Path": "run/utmp",
                "RiskLevel": "4",
                "Category": "Category",
                "VirusName": "stargate.lock",
                "Tags": [
                    "tag2"
                ],
                "Desc": "Desc",
                "Solution": "Solution",
                "FileType": "UNKOWN",
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

