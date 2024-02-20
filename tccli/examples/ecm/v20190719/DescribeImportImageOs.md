**Example 1: 查询导入镜像支持的操作系统配置信息**



Input: 

```
tccli ecm DescribeImportImageOs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ImportImageOsListSupported": {
            "Windows": [
                "Windows Server 2008",
                "Windows Server 2012",
                "Windows Server 2016"
            ],
            "Linux": [
                "CentOS",
                "Ubuntu",
                "Debian",
                "OpenSUSE",
                "SUSE",
                "CoreOS",
                "FreeBSD",
                "Other Linux"
            ]
        },
        "RequestId": "ef14668d-1daa-4e98-b545-c121a5e4ef18",
        "ImportImageOsVersionSet": [
            {
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ],
                "OsVersions": [
                    "-"
                ]
            },
            {
                "OsVersions": [
                    "-"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "-"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "5",
                    "6",
                    "7"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "7"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "6",
                    "7",
                    "8",
                    "9"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "10"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "5",
                    "6",
                    "7"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "11",
                    "12"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "10",
                    "12",
                    "14",
                    "16"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsVersions": [
                    "-"
                ],
                "OsName": "CentOS 7.4 64位",
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            }
        ]
    }
}
```

