**Example 1: 获取指定id的补丁详细信息**

获取指定id的补丁详细信息

Input: 

```
tccli cwp DescribePatchInfo --cli-unfold-argument  \
    --KbId 1
```

Output: 
```
{
    "Response": {
        "KbId": 1,
        "KbNo": "KB3135456",
        "PatchName": "Windows Server 2012 R2 安全更新程序 (KB3135456)",
        "PublishTime": "2016-04",
        "ReferUrl": "https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2016/03/windows8.1-kb3135456-x64_a42c42ccae2e3dd54c0a7722fe7aecdae2e69785.msu",
        "RelateVulCveId": "CVE-2016-0088,CVE-2016-0089,CVE-2016-0090",
        "RelateVulInfoList": [
            {
                "CVSS": 9.3,
                "CveId": "CVE-2016-0088",
                "Id": 113214,
                "Label": "本地利用",
                "Level": 4,
                "Name": "Microsoft Windows Hyper-V 远程执行代码漏洞(CVE-2016-0088)",
                "PublishTime": "2016-04-13"
            },
            {
                "CVSS": 7.1,
                "CveId": "CVE-2016-0089",
                "Id": 113215,
                "Label": "本地利用",
                "Level": 3,
                "Name": "Microsoft Windows Hyper-V 信息泄露漏洞(CVE-2016-0089)",
                "PublishTime": "2016-04-13"
            },
            {
                "CVSS": 7.1,
                "CveId": "CVE-2016-0090",
                "Id": 113216,
                "Label": "本地利用",
                "Level": 3,
                "Name": "Microsoft Windows Hyper-V 信息泄露漏洞(CVE-2016-0090)",
                "PublishTime": "2016-04-13"
            }
        ],
        "RequestId": "d55784e4-3de4-43e9-9d82-caa0f3a19b09",
        "VulCount": 3
    }
}
```

