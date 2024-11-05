**Example 1: 镜像仓库查询镜像漏洞列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryVulList --cli-unfold-argument  \
    --Filters.0.ExactMatch False \
    --Filters.0.Name Level \
    --Filters.0.Values all \
    --Filters.1.ExactMatch False \
    --Filters.1.Name Tag \
    --Filters.1.Values all \
    --Id 1929935 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttackLevel": 0,
                "CVEID": "CVE-2019-5827",
                "Category": "OUT_OF_BOUNDS_WRITE",
                "CategoryType": "SYSTEM",
                "Component": "sqlite-libs",
                "Components": [
                    {
                        "FixedVersion": "0:3.26.0-15.el8",
                        "Name": "sqlite-libs",
                        "Path": "/var/sqlite/",
                        "Type": "SYSTEM",
                        "Version": "3.26.0-13.el8"
                    }
                ],
                "CvssScore": "8.8",
                "CvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H",
                "DefenseSolution": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接：https://chromereleases.googleblog.com/2019/04/stable-channel-update-for-desktop_30.html",
                "Des": "GoogleChrome是美国谷歌（Google）公司的一款Web浏览器。GoogleChrome74.0.3729.131之前版本中的SQLite存在安全漏洞。攻击者可借助特制的HTML页面利用该漏洞损坏堆。",
                "FixedVersions": "0:3.26.0-15.el8",
                "IsSuggest": "true",
                "LayerInfos": [
                    {
                        "LayerCmd": "/bin/sh -c #(nop) ADD file:805cb5e15fb6e0bb0326ca33fd2942e068863ce2a8491bb71522c652f31fb466 in / ",
                        "LayerId": "sha256:a1d0c75327776413fa0db9ed3adcdbadedc95a662eb1d360dad82bb913f8a1d1"
                    }
                ],
                "Level": "3",
                "Name": "Google Chrome 输入验证错误漏洞",
                "OfficialSolution": "升级到最新无漏洞版本",
                "POCID": "pcmgr-209472",
                "Reference": "[\"http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00085.html\", \"https://chromereleases.googleblog.com/2019/04/stable-channel-update-for-desktop_30.html\", \"https://crbug.com/952406\", \"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/CPM7VPE27DUNJLXM4F5PAAEFFWOEND6X/\", \"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/FKN4GPMBQ3SDXWB4HL45II5CZ7P2E4AI/\", \"https://seclists.org/bugtraq/2019/Aug/19\", \"https://security.gentoo.org/glsa/202003-16\", \"https://usn.ubuntu.com/4205-1/\", \"https://www.debian.org/security/2019/dsa-4500\"]",
                "SubmitTime": "2019-06-28 09:15:00",
                "Tag": [
                    "NETWORK",
                    "SYS",
                    "APP"
                ],
                "Version": "3.26.0-13.el8"
            }
        ],
        "RequestId": "c6abad1d-0c32-4fcc-af55-df63bf986470",
        "TotalCount": 211
    }
}
```

