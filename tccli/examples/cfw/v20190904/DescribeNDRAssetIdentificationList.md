**Example 1: 获取资产识别结果列表**

获取资产识别结果列表

Input: 

```
tccli cfw DescribeNDRAssetIdentificationList --cli-unfold-argument  \
    --Limit 5 \
    --Offset 0 \
    --Filters.0.Name AssetCategory \
    --Filters.0.Values Web \
    --Filters.0.OperatorType 7
```

Output: 
```
{
    "Response": {
        "AssetCategoryOptions": [
            {
                "Text": "代理服务",
                "Value": "Proxy"
            },
            {
                "Text": "基础设施",
                "Value": "Infrastructure"
            },
            {
                "Text": "数据库",
                "Value": "Database"
            },
            {
                "Text": "邮件服务",
                "Value": "Email"
            },
            {
                "Text": "文件传输与共享服务",
                "Value": "File"
            },
            {
                "Text": "大数据组件",
                "Value": "Big Data"
            },
            {
                "Text": "流媒体服务",
                "Value": "Streaming Media"
            },
            {
                "Text": "Web服务",
                "Value": "Web"
            },
            {
                "Text": "远程管理",
                "Value": "Remote Management"
            }
        ],
        "AssetCategoryStats": [
            {
                "Name": "Web",
                "Services": [
                    {
                        "Count": 1,
                        "Name": "Apache"
                    },
                    {
                        "Count": 19,
                        "Name": "HTTP"
                    },
                    {
                        "Count": 8,
                        "Name": "Nginx"
                    },
                    {
                        "Count": 2,
                        "Name": "WordPress"
                    }
                ]
            },
            {
                "Name": "Remote Management",
                "Services": [
                    {
                        "Count": 21,
                        "Name": "SSH"
                    }
                ]
            },
            {
                "Name": "File",
                "Services": [
                    {
                        "Count": 1,
                        "Name": "FTP"
                    }
                ]
            },
            {
                "Name": "Infrastructure",
                "Services": [
                    {
                        "Count": 17,
                        "Name": "DNS"
                    },
                    {
                        "Count": 22,
                        "Name": "ICMP"
                    },
                    {
                        "Count": 7,
                        "Name": "NTP"
                    },
                    {
                        "Count": 22,
                        "Name": "SNMP"
                    },
                    {
                        "Count": 6,
                        "Name": "TLS"
                    }
                ]
            }
        ],
        "Data": [
            {
                "AssetCategory": "Web",
                "AssetId": "7492522851211195136",
                "AssetService": "Nginx",
                "AssetVersion": "1.24.0",
                "FirstIdentificationTime": "2025-03-27 17:15:32",
                "IdentificationSource": "0",
                "InstanceId": "ins-7h4tvnsa",
                "InstanceName": "未命名",
                "InstanceType": "CVM",
                "Ip": "172.30.0.16",
                "IpType": "0",
                "IpVersion": "0",
                "LatestIdentificationTime": "2025-03-27 17:30:41",
                "Port": 80,
                "Protocol": "HTTP",
                "Region": "ap-guangzhou",
                "ServerAddr": "172.30.0.16:80",
                "VpcId": "vpc-adk8xm5l",
                "VpcName": "dora172.30.0.0"
            },
            {
                "AssetCategory": "Web",
                "AssetId": "12840839795048201073",
                "AssetService": "HTTP",
                "AssetVersion": "",
                "FirstIdentificationTime": "2025-03-26 15:19:43",
                "IdentificationSource": "0",
                "InstanceId": "ins-5evxkmi2",
                "InstanceName": "测试自动开启---111111",
                "InstanceType": "CVM",
                "Ip": "172.16.31.172",
                "IpType": "0",
                "IpVersion": "0",
                "LatestIdentificationTime": "2025-03-26 16:32:53",
                "Port": 22,
                "Protocol": "HTTP",
                "Region": "ap-guangzhou",
                "ServerAddr": "172.16.31.172:22",
                "VpcId": "vpc-jaiindmz",
                "VpcName": "pgp_test"
            },
            {
                "AssetCategory": "Web",
                "AssetId": "10250506092794983187",
                "AssetService": "HTTP",
                "AssetVersion": "",
                "FirstIdentificationTime": "2025-03-26 13:29:25",
                "IdentificationSource": "0",
                "InstanceId": "ins-75reeelh",
                "InstanceName": "nta-1(御界同学使用勿删)",
                "InstanceType": "CVM",
                "Ip": "172.16.10.11",
                "IpType": "0",
                "IpVersion": "0",
                "LatestIdentificationTime": "2025-03-26 18:00:48",
                "Port": 22,
                "Protocol": "HTTP",
                "Region": "ap-chengdu",
                "ServerAddr": "172.16.10.11:22",
                "VpcId": "vpc-hr01jgf2",
                "VpcName": "nta功能验证"
            },
            {
                "AssetCategory": "Web",
                "AssetId": "8428507704829084657",
                "AssetService": "HTTP",
                "AssetVersion": "",
                "FirstIdentificationTime": "2025-03-26 10:16:34",
                "IdentificationSource": "0",
                "InstanceId": "ins-ryaagylp",
                "InstanceName": "nta-2(御界同学使用勿删)",
                "InstanceType": "CVM",
                "Ip": "172.16.10.14",
                "IpType": "0",
                "IpVersion": "0",
                "LatestIdentificationTime": "2025-03-26 14:10:13",
                "Port": 80,
                "Protocol": "HTTP",
                "Region": "ap-chengdu",
                "ServerAddr": "172.16.10.14:80",
                "VpcId": "vpc-hr01jgf2",
                "VpcName": "nta功能验证"
            },
            {
                "AssetCategory": "Web",
                "AssetId": "78916800532044908",
                "AssetService": "HTTP",
                "AssetVersion": "",
                "FirstIdentificationTime": "2025-03-26 10:14:26",
                "IdentificationSource": "0",
                "InstanceId": "ins-i7lmkarv",
                "InstanceName": "自动回溯",
                "InstanceType": "CVM",
                "Ip": "172.16.1.2",
                "IpType": "0",
                "IpVersion": "0",
                "LatestIdentificationTime": "2025-03-26 19:07:18",
                "Port": 8080,
                "Protocol": "HTTP",
                "Region": "ap-chengdu",
                "ServerAddr": "172.16.1.2:8080",
                "VpcId": "vpc-hr01jgf2",
                "VpcName": "nta功能验证"
            }
        ],
        "IdentificationSourceOptions": [
            {
                "Text": "资产识别",
                "Value": "0"
            },
            {
                "Text": "云资产实例",
                "Value": "1"
            }
        ],
        "InstanceTypeOptions": [
            {
                "Text": "CVM",
                "Value": "CVM"
            }
        ],
        "IpTypeOptions": [
            {
                "Text": "弹性公网IP",
                "Value": "1"
            },
            {
                "Text": "内网IP",
                "Value": "-1"
            },
            {
                "Text": "公网IP",
                "Value": "0"
            }
        ],
        "IpVersionOptions": [
            {
                "Text": "IPv4",
                "Value": "0"
            },
            {
                "Text": "IPv6",
                "Value": "1"
            }
        ],
        "ProtocolOptions": [
            {
                "Text": "SSH",
                "Value": "SSH"
            },
            {
                "Text": "ICMP",
                "Value": "ICMP"
            },
            {
                "Text": "DNS",
                "Value": "DNS"
            },
            {
                "Text": "HTTP",
                "Value": "HTTP"
            },
            {
                "Text": "SNMP",
                "Value": "SNMP"
            },
            {
                "Text": "FTP",
                "Value": "FTP"
            },
            {
                "Text": "TLS",
                "Value": "TLS"
            },
            {
                "Text": "NTP",
                "Value": "NTP"
            }
        ],
        "RegionOptions": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "成都",
                "Value": "ap-chengdu"
            },
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            }
        ],
        "RequestId": "c3dd0162-08ad-453a-a847-a5cc162cd074",
        "Total": 30
    }
}
```

