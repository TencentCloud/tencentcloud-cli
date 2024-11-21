**Example 1: 获取cvm列表**

获取cvm列表

Input: 

```
tccli csip DescribeCVMAssets --cli-unfold-argument  \
    --Filter.Filters.0.Name ProtectStatus \
    --Filter.Filters.0.Values 4 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Filters.1.Name TimeRange \
    --Filter.Filters.1.Values 2 \
    --Filter.Filters.1.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By AssetCreateTime \
    --MemberId mem-5b28e2010c18f07a
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "125000001",
                "Value": "130200001"
            }
        ],
        "AssetMapInstanceTypeList": [
            {
                "Text": "主机",
                "Value": "Instance",
                "InstanceTypeList": [
                    {
                        "Text": "CVM",
                        "Value": "CVM"
                    }
                ]
            }
        ],
        "AssetTypeList": [
            {
                "Text": "CVM",
                "Value": "CVM"
            }
        ],
        "Data": [
            {
                "AssetId": "ins-ggrnxdwj",
                "AssetName": "主机测试2-win",
                "PublicIp": "139.*.*.171",
                "PrivateIp": "172.16.0.9",
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "IsCore": 2,
                "AssetType": "CVM",
                "Region": "ap-chengdu",
                "AvailableArea": "成都一区",
                "Os": "Windows Server 2012 R2 数据中心版 64位中文版",
                "VpcId": "vpc-pr0wcl5e",
                "VpcName": "fengqqian",
                "OsName": "Windows Server 2012 R2 数据中心版 64位中文版",
                "CPUInfo": "AMD EPYC 7K83 64-Core Processor",
                "CPUSize": 2,
                "CPULoad": "未知",
                "MemorySize": "4GB",
                "MemoryLoad": "34.21%",
                "DiskSize": "49GB",
                "DiskLoad": "29.13%",
                "PartitionCount": 2,
                "AppId": 1302396215,
                "Uin": "100014592178",
                "SubnetId": "subnet-hn32qgp5",
                "SubnetName": "fengsub",
                "InstanceUuid": "82727b6e-3676-4660-ac4e-c281dba1b23f",
                "InstanceQUuid": "82727b6e-3676-4660-ac4e-c281dba1b23f",
                "NickName": "nickname",
                "AccountCount": "2",
                "ProcessCount": "41",
                "AppCount": "1",
                "PortCount": 19,
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "ConfigurationRisk": 52,
                "LastScanTime": "2024-10-30 05:02:29",
                "AssetCreateTime": "2024-10-28 19:36:43",
                "BASAgentStatus": -1,
                "CWPStatus": 4,
                "ProtectStatus": 4,
                "Attack": 0,
                "Access": 0,
                "Intercept": 0,
                "NetWorkOut": 0,
                "RiskExposure": 0,
                "ScanTask": 1,
                "MemberId": "mem-625c522c0913c901",
                "IsNewAsset": 0,
                "CVMStatus": 1,
                "CVMAgentStatus": 1,
                "DefenseModel": 1,
                "TatStatus": 1,
                "AgentStatus": 1,
                "CloseDefenseCount": 0,
                "CpuTrend": [
                    {
                        "Key": "2024-10-29 07:45:16",
                        "Value": "0.5208333"
                    },
                    {
                        "Key": "2024-10-29 23:43:52",
                        "Value": "0.26041666"
                    }
                ],
                "MemoryTrend": [
                    {
                        "Key": "2024-10-29 07:45:16",
                        "Value": "24"
                    },
                    {
                        "Key": "2024-10-29 23:43:52",
                        "Value": "32"
                    }
                ],
                "InstanceState": "RUNNING",
                "SecurityGroupIds": [
                    "sg-ijs188uj"
                ],
                "AgentCpuPer": 0,
                "AgentMemRss": 26088,
                "RealAppid": 0,
                "CloudType": 0,
                "OfflineTime": "2024-10-29 23:43:52"
            },
            {
                "AssetId": "ins-m1xkxkv4",
                "AssetName": "linux-arm-foo",
                "PublicIp": "119.*.*.202",
                "PrivateIp": "10.10.0.48",
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "IsCore": 2,
                "AssetType": "CVM",
                "Region": "ap-guangzhou",
                "AvailableArea": "广州六区",
                "Os": "Ubuntu 18.04(arm64)",
                "VpcId": "vpc-fw2ndu5f",
                "VpcName": "arm-vpc",
                "OsName": "Ubuntu 18.04(arm64)",
                "CPUInfo": "AMD EPYC 7K83 64-Core Processor",
                "CPUSize": 2,
                "CPULoad": "低",
                "MemorySize": "4GB",
                "MemoryLoad": "14.41%",
                "DiskSize": "146GB",
                "DiskLoad": "36.94%",
                "PartitionCount": 5,
                "AppId": 1302396215,
                "Uin": "100014592178",
                "SubnetId": "subnet-jol7wxbs",
                "SubnetName": "fengsub",
                "InstanceUuid": "e868e2da-8c44-4037-b4dd-daf790edf7a4",
                "InstanceQUuid": "e868e2da-8c44-4037-b4dd-daf790edf7a4",
                "NickName": "声声乌龙",
                "AccountCount": "32",
                "ProcessCount": "34",
                "AppCount": "5",
                "PortCount": 7,
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "ConfigurationRisk": 1,
                "LastScanTime": "2024-10-30 05:02:29",
                "AssetCreateTime": "2024-09-26 11:28:19",
                "BASAgentStatus": 0,
                "CWPStatus": 4,
                "ProtectStatus": 4,
                "Attack": 0,
                "Access": 0,
                "Intercept": 0,
                "NetWorkOut": 0,
                "RiskExposure": 0,
                "ScanTask": 14,
                "MemberId": "mem-625c522c0913c901",
                "IsNewAsset": 0,
                "CVMStatus": 1,
                "CVMAgentStatus": 1,
                "DefenseModel": 1,
                "TatStatus": 1,
                "AgentStatus": 1,
                "CloseDefenseCount": 0,
                "CpuTrend": [
                    {
                        "Key": "2024-10-29 07:45:16",
                        "Value": "0.5208333"
                    },
                    {
                        "Key": "2024-10-29 23:43:52",
                        "Value": "0.26041666"
                    }
                ],
                "MemoryTrend": [
                    {
                        "Key": "2024-10-29 07:45:16",
                        "Value": "24"
                    },
                    {
                        "Key": "2024-10-29 23:43:52",
                        "Value": "32"
                    }
                ],
                "InstanceState": "RUNNING",
                "SecurityGroupIds": [
                    "sg-biz3919h"
                ],
                "AgentCpuPer": 0,
                "AgentMemRss": 0,
                "RealAppid": 0,
                "CloudType": 0,
                "OfflineTime": "2024-10-"
            },
            {
                "AssetId": "ins-p7x4hn7p",
                "AssetName": "自动化测试",
                "PublicIp": "132.*.*.102",
                "PrivateIp": "10.0.0.11",
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "IsCore": 2,
                "AssetType": "CVM",
                "Region": "ap-chengdu",
                "AvailableArea": "成都一区",
                "Os": "TencentOS Server 3.1 (TK4)",
                "VpcId": "vpc-iozrpgxo",
                "VpcName": "自动化测试",
                "OsName": "TencentOS Server 3.1 (TK4)",
                "CPUInfo": "Intel(R) Xeon(R) Platinum 8255C CPU @ 2.50GHz",
                "CPUSize": 2,
                "CPULoad": "低",
                "MemorySize": "2GB",
                "MemoryLoad": "22.72%",
                "DiskSize": "49GB",
                "DiskLoad": "18.62%",
                "PartitionCount": 1,
                "AppId": 1302396215,
                "Uin": "100014592178",
                "SubnetId": "subnet-5fect5mp",
                "SubnetName": "fengsub1",
                "InstanceUuid": "7a6eaa66-0f21-45c1-a33c-d89ca32d2866",
                "InstanceQUuid": "7a6eaa66-0f21-45c1-a33c-d89ca32d2866",
                "NickName": "声声乌龙",
                "AccountCount": "32",
                "ProcessCount": "30",
                "AppCount": "5",
                "PortCount": 4,
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "ConfigurationRisk": 7,
                "LastScanTime": "2024-10-30 05:02:29",
                "AssetCreateTime": "2024-09-09 20:34:02",
                "BASAgentStatus": 1,
                "CWPStatus": 4,
                "ProtectStatus": 4,
                "Attack": 0,
                "Access": 0,
                "Intercept": 0,
                "NetWorkOut": 0,
                "RiskExposure": 0,
                "ScanTask": 24,
                "MemberId": "mem-625c522c0913c901",
                "IsNewAsset": 0,
                "CVMStatus": 1,
                "CVMAgentStatus": 1,
                "DefenseModel": 1,
                "TatStatus": 1,
                "AgentStatus": 1,
                "CloseDefenseCount": 0,
                "CpuTrend": [
                    {
                        "Key": "2024-10-29 07:45:16",
                        "Value": "0.5208333"
                    },
                    {
                        "Key": "2024-10-29 23:43:52",
                        "Value": "0.26041666"
                    }
                ],
                "MemoryTrend": [
                    {
                        "Key": "2024-10-29 07:45:16",
                        "Value": "24"
                    },
                    {
                        "Key": "2024-10-29 23:43:52",
                        "Value": "32"
                    }
                ],
                "InstanceState": "RUNNING",
                "SecurityGroupIds": [
                    "sg-ijs188uj"
                ],
                "AgentCpuPer": 1.50754,
                "AgentMemRss": 124244,
                "RealAppid": 0,
                "CloudType": 0,
                "OfflineTime": "2024-10-03 11:29:11"
            }
        ],
        "DefenseStatusList": [
            {
                "Text": "基础版未防护",
                "Value": "2"
            },
            {
                "Text": "旗舰版防护中",
                "Value": "4"
            }
        ],
        "IpTypeList": [
            {
                "Text": "公网资产",
                "Value": "1"
            },
            {
                "Text": "私网资产",
                "Value": "0"
            }
        ],
        "OsList": [
            {
                "Text": "CentOS",
                "Value": "1"
            },
            {
                "Text": "Windows Server",
                "Value": "6"
            },
            {
                "Text": "TencentOS",
                "Value": "7"
            },
            {
                "Text": "Ubuntu",
                "Value": "5"
            },
            {
                "Text": "CoreOS",
                "Value": "8"
            },
            {
                "Text": "Debian",
                "Value": "2"
            }
        ],
        "ProtectStatusList": [
            {
                "Text": "未安装",
                "Value": "0"
            },
            {
                "Text": "基础版防护中",
                "Value": "1"
            },
            {
                "Text": "普惠版防护中",
                "Value": "2"
            },
            {
                "Text": "专业版防护中",
                "Value": "3"
            },
            {
                "Text": "旗舰版防护中",
                "Value": "4"
            },
            {
                "Text": "已离线",
                "Value": "5"
            },
            {
                "Text": "已关机",
                "Value": "6"
            }
        ],
        "PublicPrivateAttr": [
            {
                "Text": "内网服务",
                "Value": "0"
            },
            {
                "Text": "公网服务",
                "Value": "1"
            }
        ],
        "RegionList": [
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "成都",
                "Value": "ap-chengdu"
            },
            {
                "Text": "硅谷",
                "Value": "na-siliconvalley"
            },
            {
                "Text": "北京",
                "Value": "ap-beijing"
            },
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            }
        ],
        "RequestId": "4a537d7d-0562-4fe8-8f62-6028777279eb",
        "SystemTypeList": [
            {
                "Text": "linux",
                "Value": "linux"
            },
            {
                "Text": "windows",
                "Value": "windows"
            }
        ],
        "Total": 3,
        "VpcList": [
            {
                "Text": "li-vr",
                "Value": "vpc-gu5j0xuy"
            },
            {
                "Text": "fengqqian",
                "Value": "vpc-pr0wcl5e"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-6bmvfm3h"
            },
            {
                "Text": "li-跨账号2",
                "Value": "vpc-1hezruby"
            },
            {
                "Text": "fengqqian2",
                "Value": "vpc-fw2ndu5f"
            },
            {
                "Text": "fengqqian",
                "Value": "vpc-294np9d5"
            },
            {
                "Text": "自动化测试请勿删除",
                "Value": "vpc-iozrpgxo"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-ommo5hlv"
            },
            {
                "Text": "vpc-gz-0",
                "Value": "vpc-68t3zm89"
            }
        ],
        "ZoneList": [
            {
                "Text": "上海五区",
                "Value": "ap-shanghai-5"
            },
            {
                "Text": "成都一区",
                "Value": "ap-chengdu-1"
            },
            {
                "Text": "硅谷一区",
                "Value": "na-siliconvalley-1"
            },
            {
                "Text": "北京七区",
                "Value": "ap-beijing-7"
            },
            {
                "Text": "广州六区",
                "Value": "ap-guangzhou-6"
            },
            {
                "Text": "广州三区",
                "Value": "ap-guangzhou-3"
            }
        ]
    }
}
```

