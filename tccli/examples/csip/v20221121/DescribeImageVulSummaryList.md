**Example 1: 查询镜像漏洞概览列表**



Input: 

```
tccli csip DescribeImageVulSummaryList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "ImageVulSummaryList": [
            {
                "AffectImageCount": 58,
                "FirstFoundTime": "2026-07-25T17:19:53+08:00",
                "ID": 412,
                "LatestFoundTime": "2026-08-12T20:58:03+08:00",
                "OwnerAccountName": "***-*理*",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "VulInfo": {
                    "AffectProduct": "libxml2",
                    "AffectVendor": "xmlsoft",
                    "CVEID": "CVE-2016-3709",
                    "CVSSLevel": "MEDIUM",
                    "Category": "LINUX",
                    "CheckMethod": "VersionCompare",
                    "CvssScore": "6.1",
                    "DefendStatus": "NOT_ENABLED",
                    "EPSSScore": 0.00116,
                    "FixSolution": "建议您更新当前系统或软件至最新版，完成漏洞的修复。",
                    "KVERecord": false,
                    "Label": [
                        "远程利用"
                    ],
                    "Mechanism": "",
                    "Name": "libxml2 跨站脚本漏洞(CVE-2016-3709)",
                    "PocId": "TVD-2016-17163",
                    "Precondition": "利用此漏洞需交互\n",
                    "PublishTime": "2022-07-29 01:15:00",
                    "RefLink": "https://mail.gnome.org/archives/xml/2018-January/msg00010.html",
                    "Remark": "",
                    "Summary": "libxml2是开源的一个用来解析XML文档的函数库。它用C语言写成，并且能为多种语言所调用，例如C语言，C++，XSH。 libxml2 存在安全漏洞，该漏洞源于提交960f0e2后libxml中可能存在跨站脚本漏洞。",
                    "SupportFix": true
                }
            }
        ],
        "TotalCount": 419,
        "RequestId": "304f8470-3cff-4b48-997c-02281cd21e22"
    }
}
```

