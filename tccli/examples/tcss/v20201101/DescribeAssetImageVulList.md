**Example 1: 查询镜像漏洞列表**



Input: 

```
tccli tcss DescribeAssetImageVulList --cli-unfold-argument  \
    --ImageID csnjkcnshj
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "AttackLevel": 0,
                "CVEID": "CVE-2016-5131",
                "CVSSV3Desc": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H",
                "CVSSV3Score": 8.8,
                "Category": "CODE_INJECTION",
                "CategoryType": "SYSTEM",
                "Component": "libxml2",
                "DefenseSolution": "建议您更新当前系统或软件至最新版，完成漏洞的修复。",
                "Des": "GoogleChrome是美国谷歌（Google）公司开发的一款Web浏览器。Libxml2是其中的一个基于C语言的用来解析XML文档的函数库组件。GoogleChrome52.0.2743.82之前版本中使用的libxml22.9.4及之前的版本存在释放后重用漏洞。远程攻击者可利用该漏洞造成拒绝服务。",
                "FixedVersions": "0:2.9.1-6.tl2.4",
                "IsSuggest": true,
                "Level": 2,
                "Name": "libxml2 释放后重用漏洞 (CVE-2016-5131)",
                "OfficialSolution": "升级到最新无漏洞版本",
                "Reference": "[\"http://googlechromereleases.blogspot.com/2016/07/stable-channel-update.html\", \"http://lists.apple.com/archives/security-announce/2016/Sep/msg00006.html\", \"http://lists.apple.com/archives/security-announce/2016/Sep/msg00008.html\", \"http://lists.apple.com/archives/security-announce/2016/Sep/msg00010.html\", \"http://lists.apple.com/archives/security-announce/2016/Sep/msg00011.html\", \"http://lists.opensuse.org/opensuse-security-announce/2016-07/msg00020.html\", \"http://lists.opensuse.org/opensuse-security-announce/2016-07/msg00021.html\", \"http://lists.opensuse.org/opensuse-security-announce/2016-07/msg00022.html\", \"http://lists.opensuse.org/opensuse-security-announce/2016-07/msg00028.html\", \"http://rhn.redhat.com/errata/RHSA-2016-1485.html\", \"http://www.debian.org/security/2016/dsa-3637\", \"http://www.securityfocus.com/bid/92053\", \"http://www.securitytracker.com/id/1036428\", \"http://www.securitytracker.com/id/1038623\", \"http://www.ubuntu.com/usn/USN-3041-1\", \"https://bugzilla.redhat.com/show_bug.cgi?id=1358641\", \"https://codereview.chromiu\"]",
                "SubmitTime": "2016-07-24T11:59:00+08:00",
                "Tag": [
                    "NETWORK"
                ],
                "Version": "2.9.1-6.tl2.3"
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

