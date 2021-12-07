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
        "TotalCount": 2,
        "List": [
            {
                "Category": "xx",
                "CVEID": "CVE-2018-1000500",
                "Name": "Sudo 安全漏洞",
                "Reference": "[\"https://bugzilla.suse.com/show_bug.cgi?id=CVE-2021-23240\", \"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/EE42Y35SMJOLONAIBNYNFC7J44UUZ2Y6/\", \"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/GMY4VSSBIND7VAYSN6T7XIWJRWG4GBB3/\", \"https://security.gentoo.org/glsa/202101-33\", \"https://www.sudo.ws/stable.html#1.9.5\"]",
                "Level": 1,
                "CVSSV3Score": 7.800000190734863,
                "Des": "Sudo是一款使用于类Unix系统的，允许用户通过安全的方式使用特殊的权限执行命令的程序。sudo1.9.4.p2-2版本存在安全漏洞，攻击者可利用该漏洞使用sudoedit来更改任意文件的所有权。",
                "Component": "sudo",
                "IsSuggest": true,
                "SubmitTime": "2021-01-12T09:15:00Z",
                "Version": "1.9.0-r0",
                "DefenseSolution": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接:https://www.sudo.ws/repos/sudo/rev/8fcb36ef422a",
                "OfficialSolution": "",
                "CategoryType": "其他",
                "CVSSV3Desc": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H"
            },
            {
                "Category": "资料不足",
                "CVEID": "CVE-2021-23240",
                "Name": "Busybox 安全漏洞",
                "Reference": "[\"https://bugzilla.suse.com/show_bug.cgi?id=CVE-2021-23240\", \"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/EE42Y35SMJOLONAIBNYNFC7J44UUZ2Y6/\", \"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/GMY4VSSBIND7VAYSN6T7XIWJRWG4GBB3/\", \"https://security.gentoo.org/glsa/202101-33\", \"https://www.sudo.ws/stable.html#1.9.5\"]",
                "Level": 3,
                "CVSSV3Score": 8.100000381469727,
                "Des": "<p>BusyBox是乌克兰软件开发者DenisVlasenko所负责维护的一套包含了多个linux命令和工具的应用程序。Busybox在“ busybox wget”小程序中包含一个缺少SSL证书验证漏洞，该漏洞可能导致任意代码执行。通过使用“ busybox wget https://compromised-domain.com/important-file”通过HTTPS下载任何文件，似乎可以利用此攻击。</p>",
                "Component": "busybox",
                "IsSuggest": true,
                "SubmitTime": "2018-06-26T16:29:00Z",
                "Version": "1.31.1-r16",
                "DefenseSolution": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接：https://git.busybox.net/busybox/tree/networking/wget.c?id=8bc418f07eab79a9c8d26594629799f6157a9466#n74",
                "OfficialSolution": "<p>升级到最新无漏洞版本</p>",
                "CategoryType": "web应用漏洞",
                "CVSSV3Desc": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H"
            }
        ],
        "RequestId": "f29aaf0b-acde-40e2-9ce8-c517265c0ff3"
    }
}
```

