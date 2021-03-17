**Example 1: 获取基础配置**

获取基础配置

Input: 

```
tccli ecm DescribeConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceNetworkLimitConfigs": [
            {
                "CpuNum": 1,
                "NetworkInterfaceLimit": 2,
                "InnerIpPerNetworkInterface": 2,
                "PublicIpPerInstance": 1
            },
            {
                "CpuNum": 2,
                "NetworkInterfaceLimit": 2,
                "InnerIpPerNetworkInterface": 10,
                "PublicIpPerInstance": 1
            },
            {
                "CpuNum": 4,
                "NetworkInterfaceLimit": 3,
                "InnerIpPerNetworkInterface": 10,
                "PublicIpPerInstance": 3
            },
            {
                "CpuNum": 8,
                "NetworkInterfaceLimit": 4,
                "InnerIpPerNetworkInterface": 10,
                "PublicIpPerInstance": 3
            },
            {
                "CpuNum": 16,
                "NetworkInterfaceLimit": 6,
                "InnerIpPerNetworkInterface": 10,
                "PublicIpPerInstance": 4
            },
            {
                "CpuNum": 24,
                "NetworkInterfaceLimit": 6,
                "InnerIpPerNetworkInterface": 10,
                "PublicIpPerInstance": 4
            },
            {
                "CpuNum": 32,
                "NetworkInterfaceLimit": 8,
                "InnerIpPerNetworkInterface": 20,
                "PublicIpPerInstance": 4
            },
            {
                "CpuNum": 48,
                "NetworkInterfaceLimit": 8,
                "InnerIpPerNetworkInterface": 20,
                "PublicIpPerInstance": 4
            },
            {
                "CpuNum": 64,
                "NetworkInterfaceLimit": 8,
                "InnerIpPerNetworkInterface": 20,
                "PublicIpPerInstance": 4
            },
            {
                "CpuNum": 96,
                "NetworkInterfaceLimit": 8,
                "InnerIpPerNetworkInterface": 20,
                "PublicIpPerInstance": 4
            },
            {
                "CpuNum": 128,
                "NetworkInterfaceLimit": 8,
                "InnerIpPerNetworkInterface": 20,
                "PublicIpPerInstance": 4
            },
            {
                "CpuNum": 256,
                "NetworkInterfaceLimit": 8,
                "InnerIpPerNetworkInterface": 20,
                "PublicIpPerInstance": 4
            }
        ],
        "DefaultIPDirect": true,
        "NetworkStorageRange": {
            "PerBandwidth": 1,
            "MaxDataDiskSize": 1024,
            "SuggestSystemDiskSize": 50,
            "MinDataDiskSize": 50,
            "MaxVcpuPerReq": 100,
            "SuggestBandwidth": 25,
            "MaxModuleNum": 1000,
            "PerDataDisk": 10,
            "MinSystemDiskSize": 0,
            "SuggestDataDiskSize": 1024,
            "MaxVcpu": 100,
            "MinBandwidth": 25,
            "MaxSystemDiskSize": 100,
            "MinVcpu": 1,
            "MaxBandwidth": 1000
        },
        "ImageLimits": {
            "MaxImageSize": 0
        },
        "RequestId": "xx",
        "ImageWhiteSet": [
            "CentOS 6.2 64",
            "CentOS 6.3 64",
            "CentOS 6.8 64",
            "CentOS 6.9 32",
            "CentOS 6.9 64",
            "CentOS 7.2 64",
            "CentOS 7.3 64",
            "CentOS 7.4 64",
            "CentOS 7.5 64",
            "CentOS 7.6 64",
            "Debian 7.4 64",
            "Debian 8.2 32",
            "Debian 8.2 64",
            "Debian 9.0 64",
            "Tencent Linux Release 1.2 (tkernel2)",
            "Tencent Linux Release 2.2 (Final)",
            "Tencent Linux release 2.4 (Final)",
            "Ubuntu Server 14.04.1 LTS 32",
            "Ubuntu Server 14.04.1 LTS 64",
            "Ubuntu Server 16.04.1 LTS 32",
            "Ubuntu Server 16.04.1 LTS 64",
            "Ubuntu Server 18.04.1 LTS 64",
            "Ubuntu 16.0 64",
            "Windows Server 2012 R2",
            "Windows Server 2012 数据中心版 64位英文版",
            "Windows Server 2016 数据中心版 64位英文版",
            "Windows Server 2016 数据中心版 64位中文版",
            "None 2.2 64",
            "CentOS 8.0 64",
            "CentOS 7.7 64",
            "Windows Server 2019",
            "Debian 10.2 64",
            "Tencent tlinux release 2.2",
            "Ubuntu Server 20.04",
            "Tencent Linux release 2.6"
        ]
    }
}
```

