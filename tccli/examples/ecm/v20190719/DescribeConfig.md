**Example 1: 获取基础配置**

获取基础配置

Input: 

```
tccli ecm DescribeConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "46afa5e7-3779-477c-adc0-8241a8e96115",
        "NetworkStorageRange": {
            "MinBandwidth": 25,
            "MaxBandwidth": 3000,
            "PerBandwidth": 1,
            "SuggestBandwidth": 25,
            "MinSystemDiskSize": 50,
            "MaxSystemDiskSize": 50,
            "SuggestSystemDiskSize": 50,
            "MinDataDiskSize": 0,
            "MaxDataDiskSize": 1000,
            "PerDataDisk": 10,
            "SuggestDataDiskSize": 0,
            "MinVcpu": 1,
            "MaxVcpu": 5000,
            "MaxVcpuPerReq": 5000,
            "MaxModuleNum": 100
        },
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
            "Ubuntu Server 14.04.1 LTS 32",
            "Ubuntu Server 14.04.1 LTS 64",
            "Ubuntu Server 16.04.1 LTS 32",
            "Ubuntu Server 16.04.1 LTS 64",
            "Ubuntu Server 18.04.1 LTS 64",
            "Ubuntu 16.0 64",
            "Windows Server 2012 R2"
        ]
    }
}
```

