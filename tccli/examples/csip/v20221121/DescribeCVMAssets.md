**Example 1: cvm列表**

cvm列表

Input: 

```
tccli csip DescribeCVMAssets --cli-unfold-argument  \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc
```

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
                "Text": "边缘计算机器(ECM)",
                "Value": "ECM"
            },
            {
                "Text": "腾讯云服务器(CVM)",
                "Value": "CVM"
            }
        ],
        "Data": [
            {
                "Access": 0,
                "AccountCount": "-",
                "AppCount": "-",
                "AppId": 1300448058,
                "AssetCreateTime": "2023-02-16 16:51:34",
                "AssetId": "ein-b41zgmgq",
                "AssetName": "test1",
                "AssetType": "ECM",
                "Attack": 0,
                "AvailableArea": "",
                "CPUInfo": "",
                "CPULoad": "低",
                "CPUSize": 0,
                "CWPStatus": 1,
                "ConfigurationRisk": 0,
                "DiskLoad": "0.00%",
                "DiskSize": "0GB",
                "InBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "InstanceQUuid": "40b8a793-1e96-4101-b832-1f973b8efdb7",
                "InstanceUuid": "",
                "Intercept": 0,
                "IsCore": 1,
                "LastScanTime": "2023-03-31 17:40:20",
                "MemberId": "mem-c957e6a7195c85e0",
                "MemoryLoad": "0.00%",
                "MemorySize": "0GB",
                "NetWorkOut": 0,
                "NickName": "天空之蓝",
                "Os": "CentOS 8.0 64bit",
                "OsName": "CentOS 8.0 64bit",
                "OutBandwidth": "0.00bps",
                "OutFlow": "0.00B",
                "PartitionCount": 0,
                "PortCount": 0,
                "PortRisk": 0,
                "PrivateIp": "10.212.0.4",
                "ProcessCount": "-",
                "PublicIp": "119.147.20.109",
                "Region": "ap-guangzhou",
                "ScanTask": 13,
                "SubnetId": "subnet-0aos839s",
                "SubnetName": "",
                "Tag": [
                    {
                        "Name": "测试A",
                        "Value": "测试B"
                    }
                ],
                "Uin": "100011616646",
                "VpcId": "vpc-4c9w05r5",
                "VpcName": "",
                "VulnerabilityRisk": 0
            }
        ],
        "DefenseStatusList": [
            {
                "Text": "未开通防护",
                "Value": "1"
            },
            {
                "Text": "基础版未防护",
                "Value": "2"
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
                "Text": "未知",
                "Value": "0"
            },
            {
                "Text": "TencentOS",
                "Value": "7"
            },
            {
                "Text": "Ubuntu",
                "Value": "5"
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "北京",
                "Value": "ap-beijing"
            },
            {
                "Text": "成都",
                "Value": "ap-chengdu"
            },
            {
                "Text": "南京",
                "Value": "ap-nanjing"
            }
        ],
        "RequestId": "71673908-8c7d-41c3-8564-57c741ed3596",
        "SystemTypeList": [
            {
                "Text": "linux",
                "Value": "linux"
            }
        ],
        "Total": 29,
        "VpcList": [
            {
                "Text": "跨租户天空之蓝",
                "Value": "vpc-f6xj8nho"
            },
            {
                "Text": "成都sdwan",
                "Value": "vpc-ebfqtnxa"
            },
            {
                "Text": "冲突sdwan",
                "Value": "vpc-dw314am3"
            },
            {
                "Text": "vpctest",
                "Value": "vpc-rkm452h0"
            },
            {
                "Text": "Default-VPC很长的很长的231321321321321313",
                "Value": "vpc-5vcbd7cv"
            }
        ],
        "ZoneList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "北京",
                "Value": "ap-beijing"
            },
            {
                "Text": "成都",
                "Value": "ap-chengdu"
            },
            {
                "Text": "南京",
                "Value": "ap-nanjing"
            }
        ]
    }
}
```

