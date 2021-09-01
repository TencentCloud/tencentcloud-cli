**Example 1: 查询操作系统信息**



Input: 

```
tccli bm DescribeOsInfo --cli-unfold-argument  \
    --DeviceClassCode PS100v1
```

Output: 
```
{
    "Response": {
        "OsInfoSet": [
            {
                "OsTypeId": 85,
                "OsName": "BM-ubuntu16.04-test",
                "OsDescription": "ubuntu16.04-test",
                "OsEnglishDescription": "ubuntu16.04-test",
                "OsClass": "ubuntu",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 23,
                "OsName": "BM-ubuntu16.04",
                "OsDescription": "ubuntu 16 64位",
                "OsEnglishDescription": "ubuntu 16 64bit",
                "OsClass": "ubuntu",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 9,
                "OsName": "BM-ubuntu14",
                "OsDescription": "ubuntu 14   64位",
                "OsEnglishDescription": "ubuntu 14   64bit",
                "OsClass": "ubuntu",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 50,
                "OsName": "BM-tlinux1.2-ori",
                "OsDescription": "tlinux1.2-ori（内部版）",
                "OsEnglishDescription": "tlinux1.2-ori（内部版）",
                "OsClass": "Tlinux",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 51,
                "OsName": "BM-shuteng-centos7.2",
                "OsDescription": "shuteng-centos7.2(内部版)",
                "OsEnglishDescription": "shuteng-centos7.2(内部版)",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 52,
                "OsName": "BM-shuteng-centos7.2",
                "OsDescription": "shuteng-centos7.2",
                "OsEnglishDescription": "shuteng-centos7.2",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 57,
                "OsName": "BM-shunfeng-centos7.2",
                "OsDescription": "shunfeng-centos7.2（内部版）",
                "OsEnglishDescription": "shunfeng-centos7.2",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 56,
                "OsName": "BM-shunfeng-centos7.2",
                "OsDescription": "shunfeng-centos7.2",
                "OsEnglishDescription": "shunfeng-centos7.2",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 50
            },
            {
                "OsTypeId": 79,
                "OsName": "BM-douban-gentoo",
                "OsDescription": "gentoo 64位",
                "OsEnglishDescription": "gentoo16.7 64bit",
                "OsClass": "gentoo",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 84,
                "OsName": "BM-douban-gentoo",
                "OsDescription": "douban-gentoo-1803(内部版)",
                "OsEnglishDescription": "douban-gentoo-1803",
                "OsClass": "gentoo",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 77,
                "OsName": "BM-centos68-180501",
                "OsDescription": "centos6.8 180501",
                "OsEnglishDescription": "centos6.8 180501",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 76,
                "OsName": "BM-centos67-180501",
                "OsDescription": "centos6.7 180501",
                "OsEnglishDescription": "centos6.7 180501",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 75,
                "OsName": "BM-centos66-180501",
                "OsDescription": "centos6.6 180501",
                "OsEnglishDescription": "centos6.6 180501",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 88,
                "OsName": "BM-XServer_V16_64",
                "OsDescription": "Windows 2016 数据中心版 64位英文版",
                "OsEnglishDescription": "Windows Server 2016 Datacenter 64-bit",
                "OsClass": "Windows",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 14,
                "OsName": "BM-XServer_V12_64",
                "OsDescription": "Windows 2012 R2 标准版 64位英文版",
                "OsEnglishDescription": "Windows Server 2012 R2 Standard 64-bit (English)",
                "OsClass": "Windows",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 70,
                "OsName": "BM-ubuntu16-180501",
                "OsDescription": "Ubuntu16 180501",
                "OsEnglishDescription": "Ubuntu16 180501",
                "OsClass": "ubuntu",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 69,
                "OsName": "BM-ubuntu14-180501",
                "OsDescription": "Ubuntu14 180501",
                "OsEnglishDescription": "Ubuntu14 180501",
                "OsClass": "ubuntu",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 68,
                "OsName": "BM-ubuntu16-base",
                "OsDescription": "Ubuntu 16（基础版）",
                "OsEnglishDescription": "Ubuntu 16 base",
                "OsClass": "ubuntu",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 67,
                "OsName": "BM-ubuntu14-base",
                "OsDescription": "Ubuntu 14（基础版）",
                "OsEnglishDescription": "Ubuntu 14 base",
                "OsClass": "ubuntu",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 24,
                "OsName": "BM-tlinux1.2-ori",
                "OsDescription": "Tlinux 1.2 origin 64位",
                "OsEnglishDescription": "BM-tlinux1.2 origin 64bi",
                "OsClass": "Tlinux",
                "ImageTag": "private",
                "MaxPartitionSize": 16
            },
            {
                "OsTypeId": 74,
                "OsName": "BM-debian82-180501",
                "OsDescription": "Debian8.2 180501",
                "OsEnglishDescription": "Debian8.2 180501",
                "OsClass": "Debian",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 73,
                "OsName": "BM-debian78-180501",
                "OsDescription": "Debian7.8 180501",
                "OsEnglishDescription": "Debian7.8 180501",
                "OsClass": "Debian",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 91,
                "OsName": "BM-debian94-base",
                "OsDescription": "Debian 9.4 64位",
                "OsEnglishDescription": "Debian 9.4 64bit",
                "OsClass": "Debian",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 7,
                "OsName": "BM-debian8.2",
                "OsDescription": "Debian 8.2  64位",
                "OsEnglishDescription": "Debian 8.2  64bit",
                "OsClass": "Debian",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 66,
                "OsName": "BM-debian82-base",
                "OsDescription": "Debian 8 （基础版）",
                "OsEnglishDescription": "Debian 8 base",
                "OsClass": "Debian",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 3,
                "OsName": "BM-debian7.8",
                "OsDescription": "Debian 7.8  64位",
                "OsEnglishDescription": "Debian 7.8  64bit",
                "OsClass": "Debian",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 65,
                "OsName": "BM-debian78-base",
                "OsDescription": "Debian 7 （基础版）",
                "OsEnglishDescription": "Debian 7 base",
                "OsClass": "Debian",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 71,
                "OsName": "BM-centos65-180501",
                "OsDescription": "Centos6.5 180501",
                "OsEnglishDescription": "Centos6.5 180501",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 47,
                "OsName": "BM-centos7.3",
                "OsDescription": "Centos 7.3 64位",
                "OsEnglishDescription": "Centos 7.3 64bit",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 50
            },
            {
                "OsTypeId": 16,
                "OsName": "BM-centos72-test",
                "OsDescription": "Centos 7.2t  64位",
                "OsEnglishDescription": "Centos 7.2t  64bit",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 2,
                "OsName": "BM-centos7.2",
                "OsDescription": "Centos 7.2  64位",
                "OsEnglishDescription": "Centos 7.2  64bit",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 50
            },
            {
                "OsTypeId": 63,
                "OsName": "BM-centos72-base",
                "OsDescription": "Centos 7 （基础版）",
                "OsEnglishDescription": "centos 7 base",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 48,
                "OsName": "BM-centos6.8",
                "OsDescription": "Centos 6.8 64位",
                "OsEnglishDescription": "Centos 6.8 64bit",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 16
            },
            {
                "OsTypeId": 49,
                "OsName": "BM-centos6.7",
                "OsDescription": "Centos 6.7 64位",
                "OsEnglishDescription": "Centos 6.7 64bit",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 16
            },
            {
                "OsTypeId": 1,
                "OsName": "BM-centos6.5",
                "OsDescription": "Centos 6.5  64位",
                "OsEnglishDescription": "Centos 6.5 64bit",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 16
            },
            {
                "OsTypeId": 64,
                "OsName": "BM-centos65-base",
                "OsDescription": "Centos 6 （基础版）",
                "OsEnglishDescription": "centos 6 base",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 72,
                "OsName": "BM-centos72-180501",
                "OsDescription": "Centos7.2 180501",
                "OsEnglishDescription": "Centos7.2 180501",
                "OsClass": "CentOS",
                "ImageTag": "public",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 78,
                "OsName": "BM-centos73-180501",
                "OsDescription": "centos7.3 180501",
                "OsEnglishDescription": "centos7.3 180501",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            },
            {
                "OsTypeId": 96,
                "OsName": "BM-centos72-180501",
                "OsDescription": "Centos7.2 180501 64位 (内部版)",
                "OsEnglishDescription": "Centos7.2 180501 64bit",
                "OsClass": "CentOS",
                "ImageTag": "private",
                "MaxPartitionSize": 1000000
            }
        ],
        "RequestId": "63aafcac-21a3-48a8-9071-090dca3605aa"
    }
}
```

