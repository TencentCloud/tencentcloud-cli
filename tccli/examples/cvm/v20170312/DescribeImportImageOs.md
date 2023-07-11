**Example 1: 查询导入镜像支持的操作系统配置信息**

查询导入镜像支持的操作系统配置信息

Input: 

```
tccli cvm DescribeImportImageOs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ImportImageOsListSupported": {
            "Linux": [
                "CentOS",
                "Ubuntu",
                "Debian",
                "OpenSUSE",
                "SUSE",
                "CoreOS",
                "FreeBSD",
                "Other Linux"
            ],
            "Windows": [
                "Windows Server 2008",
                "Windows Server 2012",
                "Windows Server 2016"
            ]
        },
        "ImportImageOsVersionSet": [
            {
                "OsName": "Windows Server 2008",
                "OsVersions": [
                    "-"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "Windows Server 2012",
                "OsVersions": [
                    "-"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "Windows Server 2016",
                "OsVersions": [
                    "-"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "CentOS",
                "OsVersions": [
                    "5",
                    "6",
                    "7"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "CoreOS",
                "OsVersions": [
                    "7"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "Debian",
                "OsVersions": [
                    "6",
                    "7",
                    "8",
                    "9"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "FreeBSD",
                "OsVersions": [
                    "10"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "Redhat",
                "OsVersions": [
                    "5",
                    "6",
                    "7"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "OpenSUSE",
                "OsVersions": [
                    "11",
                    "12"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "SUSE",
                "OsVersions": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "Ubuntu",
                "OsVersions": [
                    "10",
                    "12",
                    "14",
                    "16"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            },
            {
                "OsName": "Other Linux",
                "OsVersions": [
                    "-"
                ],
                "Architecture": [
                    "x86_64",
                    "i386"
                ]
            }
        ],
        "RequestId": "32064a8f-8d3f-4670-8d4f-60123ca97042"
    }
}
```

