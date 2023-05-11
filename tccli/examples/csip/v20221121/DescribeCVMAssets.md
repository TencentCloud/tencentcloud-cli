**Example 1: cvm列表**

cvm列表

Input: 

```
tccli csip DescribeCVMAssets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1300448058",
                "Value": "1300448058"
            }
        ],
        "AssetTypeList": [
            {
                "Text": "腾讯云服务器(CVM)",
                "Value": "CVM"
            }
        ],
        "Data": [
            {
                "Access": 0,
                "AccountCount": "0",
                "AppCount": "0",
                "AppId": 1300448058,
                "AssetCreateTime": "2020-11-24 08:47:17",
                "AssetId": "ins-17ye5faf",
                "AssetName": "[autotest][勿删]自动化测试VPC",
                "AssetType": "CVM",
                "Attack": 0,
                "AvailableArea": "上海三区",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 2,
                "ConfigurationRisk": 0,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 1,
                "LastScanTime": "2023-02-03 14:48:17",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝-现网",
                "OsName": "",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 0,
                "PrivateIp": "10.5.1.4",
                "ProcessCount": "0",
                "PublicIp": "81.69.38.139",
                "Region": "ap-shanghai",
                "ScanTask": 13,
                "SubnetId": "subnet-cjxihpy1",
                "SubnetName": "[autotest][勿删]自动化测试B2",
                "Tag": [
                    {
                        "Name": "ruri",
                        "Value": "test"
                    }
                ],
                "Uin": "100011616646",
                "VpcId": "vpc-msa9dvac",
                "VpcName": "[autotest][勿删]自动化测试B",
                "VulnerabilityRisk": 2
            },
            {
                "Access": 0,
                "AccountCount": "0",
                "AppCount": "0",
                "AppId": 1300448058,
                "AssetCreateTime": "2023-02-02 09:25:49",
                "AssetId": "ins-c2c1ebl4",
                "AssetName": "漏洞机",
                "AssetType": "CVM",
                "Attack": 0,
                "AvailableArea": "广州六区",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 2,
                "ConfigurationRisk": 0,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 1,
                "LastScanTime": "-",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝-现网",
                "OsName": "",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 0,
                "PrivateIp": "172.16.16.8",
                "ProcessCount": "0",
                "PublicIp": "43.136.112.195",
                "Region": "ap-guangzhou",
                "ScanTask": 0,
                "SubnetId": "subnet-piyq3xq0",
                "SubnetName": "Default-Subnet",
                "Tag": null,
                "Uin": "100011616646",
                "VpcId": "vpc-imk763v1",
                "VpcName": "Default-VPC",
                "VulnerabilityRisk": 5
            },
            {
                "Access": 0,
                "AccountCount": "0",
                "AppCount": "0",
                "AppId": 1300448058,
                "AssetCreateTime": "2022-10-21 01:18:03",
                "AssetId": "ins-gt3h3i8f",
                "AssetName": "[autotest][勿删]自动化测试NAT",
                "AssetType": "CVM",
                "Attack": 0,
                "AvailableArea": "上海三区",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 2,
                "ConfigurationRisk": 74,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 0,
                "LastScanTime": "2023-02-02 15:44:38",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝-现网",
                "OsName": "",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 0,
                "PrivateIp": "10.5.2.13",
                "ProcessCount": "0",
                "PublicIp": "115.159.113.26",
                "Region": "ap-shanghai",
                "ScanTask": 14,
                "SubnetId": "subnet-kdu0qj4t",
                "SubnetName": "[autotest][勿删]自动化测试B1",
                "Tag": null,
                "Uin": "100011616646",
                "VpcId": "vpc-msa9dvac",
                "VpcName": "[autotest][勿删]自动化测试B",
                "VulnerabilityRisk": 519
            },
            {
                "Access": 0,
                "AccountCount": "0",
                "AppCount": "0",
                "AppId": 1300448058,
                "AssetCreateTime": "2020-10-21 11:11:49",
                "AssetId": "ins-kja8dy5r",
                "AssetName": "[autotest][勿删]自动化测试NAT",
                "AssetType": "CVM",
                "Attack": 0,
                "AvailableArea": "上海二区",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 2,
                "ConfigurationRisk": 0,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 0,
                "LastScanTime": "2023-02-02 15:44:38",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝-现网",
                "OsName": "",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 0,
                "PrivateIp": "172.17.32.17",
                "ProcessCount": "0",
                "PublicIp": "182.254.145.158",
                "Region": "ap-shanghai",
                "ScanTask": 13,
                "SubnetId": "subnet-5sx5vrcj",
                "SubnetName": "[autotest][勿删]自动化测试A1",
                "Tag": [
                    {
                        "Name": "自动化测试-勿删",
                        "Value": "autotest"
                    }
                ],
                "Uin": "100011616646",
                "VpcId": "vpc-q9h93ip4",
                "VpcName": "[autotest][勿删]自动化测试A",
                "VulnerabilityRisk": 1
            },
            {
                "Access": 0,
                "AccountCount": "0",
                "AppCount": "0",
                "AppId": 1300448058,
                "AssetCreateTime": "2022-12-19 08:00:54",
                "AssetId": "ins-o49doo4m",
                "AssetName": "未命名",
                "AssetType": "CVM",
                "Attack": 0,
                "AvailableArea": "广州四区",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 2,
                "ConfigurationRisk": 0,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 0,
                "LastScanTime": "2023-02-02 11:42:10",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝-现网",
                "OsName": "",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 7,
                "PrivateIp": "172.16.0.14",
                "ProcessCount": "0",
                "PublicIp": "43.136.103.9",
                "Region": "ap-guangzhou",
                "ScanTask": 8,
                "SubnetId": "subnet-q6ztsegg",
                "SubnetName": "Default-Subnet",
                "Tag": null,
                "Uin": "100011616646",
                "VpcId": "vpc-imk763v1",
                "VpcName": "Default-VPC",
                "VulnerabilityRisk": 0
            },
            {
                "Access": 0,
                "AccountCount": "0",
                "AppCount": "0",
                "AppId": 1300448058,
                "AssetCreateTime": "2020-11-12 07:00:13",
                "AssetId": "ins-p1jyrg75",
                "AssetName": "[autotest][勿删]自动化测试VPC",
                "AssetType": "CVM",
                "Attack": 0,
                "AvailableArea": "上海二区",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 2,
                "ConfigurationRisk": 0,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 0,
                "LastScanTime": "2023-02-02 15:44:38",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝-现网",
                "OsName": "",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 0,
                "PrivateIp": "172.17.32.11",
                "ProcessCount": "0",
                "PublicIp": "42.192.123.209",
                "Region": "ap-shanghai",
                "ScanTask": 13,
                "SubnetId": "subnet-5sx5vrcj",
                "SubnetName": "[autotest][勿删]自动化测试A1",
                "Tag": [
                    {
                        "Name": "自动化测试-勿删",
                        "Value": "autotest"
                    }
                ],
                "Uin": "100011616646",
                "VpcId": "vpc-q9h93ip4",
                "VpcName": "[autotest][勿删]自动化测试A",
                "VulnerabilityRisk": 3
            },
            {
                "Access": 0,
                "AccountCount": "0",
                "AppCount": "0",
                "AppId": 1300448058,
                "AssetCreateTime": "2022-11-14 02:53:37",
                "AssetId": "ins-r6ou78a4",
                "AssetName": "漏扫新引擎测试-请勿动-PGP",
                "AssetType": "CVM",
                "Attack": 0,
                "AvailableArea": "南京三区",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 2,
                "ConfigurationRisk": 0,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 0,
                "LastScanTime": "2023-02-02 15:44:38",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝-现网",
                "OsName": "",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 0,
                "PrivateIp": "10.206.16.11",
                "ProcessCount": "0",
                "PublicIp": "43.137.1.67",
                "Region": "ap-nanjing",
                "ScanTask": 13,
                "SubnetId": "subnet-p311203u",
                "SubnetName": "Default-Subnet",
                "Tag": null,
                "Uin": "100011616646",
                "VpcId": "vpc-5vcbd7cv",
                "VpcName": "Default-VPC很长的很长的231321321321321313",
                "VulnerabilityRisk": 1
            }
        ],
        "DefenseStatusList": [
            {
                "Text": "基础版未防护",
                "Value": "2"
            }
        ],
        "IpTypeList": [
            {
                "Text": "公网资产",
                "Value": "1"
            }
        ],
        "RegionList": [
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "南京",
                "Value": "ap-nanjing"
            }
        ],
        "RequestId": "7c5ca068-50ab-450c-9bbe-000f6c67fbb9",
        "SystemTypeList": [
            {
                "Text": "linux",
                "Value": "linux"
            }
        ],
        "Total": 7,
        "VpcList": [
            {
                "Text": "[autotest][勿删]自动化测试B",
                "Value": "vpc-msa9dvac"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-imk763v1"
            },
            {
                "Text": "[autotest][勿删]自动化测试A",
                "Value": "vpc-q9h93ip4"
            },
            {
                "Text": "Default-VPC很长的很长的231321321321321313",
                "Value": "vpc-5vcbd7cv"
            }
        ],
        "ZoneList": [
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "南京",
                "Value": "ap-nanjing"
            }
        ]
    }
}
```

