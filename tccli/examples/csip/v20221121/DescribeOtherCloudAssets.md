**Example 1: 其他云资源列表**

其他云资源列表

Input: 

```
tccli csip DescribeOtherCloudAssets --cli-unfold-argument  \
    --Filter.Filters.0.Name TimeRange \
    --Filter.Filters.0.Values 2 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By AssetCreateTime \
    --MemberId mem-1fc116ccbc8ac7f6
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1256299843",
                "Value": "1256299843"
            }
        ],
        "AssetTypeList": [
            {
                "Text": "COS",
                "Value": "COS"
            },
            {
                "Text": "KMS",
                "Value": "KMS"
            },
            {
                "Text": "ACL",
                "Value": "ACL"
            },
            {
                "Text": "CloudAudit",
                "Value": "CloudAudit"
            },
            {
                "Text": "CFS",
                "Value": "CFS"
            },
            {
                "Text": "CKafka",
                "Value": "KAFKA"
            },
            {
                "Text": "CBS",
                "Value": "CBS"
            },
            {
                "Text": "LBL",
                "Value": "LBL"
            },
            {
                "Text": "SSL",
                "Value": "SSL"
            },
            {
                "Text": "ApiGateWay",
                "Value": "ApiGateWay"
            },
            {
                "Text": "SecurityGroup",
                "Value": "SecurityGroup"
            }
        ],
        "Data": [
            {
                "AssetId": "LP1pduRZ",
                "AssetType": "SSL",
                "Region": "ap-guangzhou",
                "VpcName": "",
                "ConfigurationRisk": 1,
                "AssetName": "",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-24 17:10:30",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 3,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 2,
                "IsNewAsset": 1
            },
            {
                "AssetId": "disk-jwie6ay5",
                "AssetType": "CBS",
                "Region": "ap-shanghai",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "L3-2_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-24 12:31:46",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 1
            },
            {
                "AssetId": "disk-jhxekap0",
                "AssetType": "CBS",
                "Region": "ap-nanjing",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "yancyw-rasp-test-2_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-24 12:17:14",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 1
            },
            {
                "AssetId": "disk-29ymdeqq",
                "AssetType": "CBS",
                "Region": "ap-nanjing",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "yancyw-rasp-test_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-24 11:33:38",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 1
            },
            {
                "AssetId": "disk-hqam7c8a",
                "AssetType": "CBS",
                "Region": "ap-guangzhou",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "v_llzlu_测试用下_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-24 11:16:22",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 1
            },
            {
                "AssetId": "disk-l5eqdsmh",
                "AssetType": "CBS",
                "Region": "ap-shanghai",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "L3 工单复现_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-23 22:12:47",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 0
            },
            {
                "AssetId": "disk-87pu7kr2",
                "AssetType": "CBS",
                "Region": "ap-hongkong",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "yancyw-rasp_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-23 21:29:50",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 0
            },
            {
                "AssetId": "disk-82u1i37o",
                "AssetType": "CBS",
                "Region": "ap-nanjing",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "baseline_test_nickpzheng_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-23 12:50:07",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 0
            },
            {
                "AssetId": "disk-2ic3oxpc",
                "AssetType": "CBS",
                "Region": "ap-guangzhou",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "tke_cls-q0bc0ed2_worker_SYSTEM_DISK",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-20 15:48:32",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 0
            },
            {
                "AssetId": "disk-ckm306h6",
                "AssetType": "CBS",
                "Region": "ap-guangzhou",
                "VpcName": "",
                "ConfigurationRisk": 0,
                "AssetName": "jimmy-test-win_系统盘",
                "VpcId": "",
                "Domain": "",
                "AssetCreateTime": "2025-06-19 18:04:40",
                "LastScanTime": "2025-06-03 20:04:30",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 0,
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "Port": 0,
                "Tag": [],
                "PrivateIp": "",
                "PublicIp": "",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 0
            }
        ],
        "RegionList": [
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "南京",
                "Value": "ap-nanjing"
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
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "清远",
                "Value": "ap-qingyuan"
            },
            {
                "Text": "法兰克福",
                "Value": "eu-frankfurt"
            },
            {
                "Text": "中国香港",
                "Value": "ap-hongkong"
            },
            {
                "Text": "新加坡",
                "Value": "ap-singapore"
            },
            {
                "Text": "上海自动驾驶云",
                "Value": "ap-shanghai-adc"
            },
            {
                "Text": "广州Open",
                "Value": "ap-guangzhou-open"
            },
            {
                "Text": "多伦多",
                "Value": "na-toronto"
            },
            {
                "Text": "北京金融",
                "Value": "ap-beijing-fsi"
            },
            {
                "Text": "重庆",
                "Value": "ap-chongqing"
            },
            {
                "Text": "长沙EC",
                "Value": "ap-changsha-ec"
            },
            {
                "Text": "曼谷",
                "Value": "ap-bangkok"
            },
            {
                "Text": "济南EC",
                "Value": "ap-jinan-ec"
            },
            {
                "Text": "东京",
                "Value": "ap-tokyo"
            },
            {
                "Text": "杭州EC",
                "Value": "ap-hangzhou-ec"
            },
            {
                "Text": "弗吉尼亚",
                "Value": "na-ashburn"
            },
            {
                "Text": "孟买",
                "Value": "ap-mumbai"
            },
            {
                "Text": "硅谷",
                "Value": "na-siliconvalley"
            },
            {
                "Text": "上海金融",
                "Value": "ap-shanghai-fsi"
            },
            {
                "Text": "福州EC",
                "Value": "ap-fuzhou-ec"
            },
            {
                "Text": "深圳金融",
                "Value": "ap-shenzhen-fsi"
            },
            {
                "Text": "首尔",
                "Value": "ap-seoul"
            },
            {
                "Text": "雅加达",
                "Value": "ap-jakarta"
            },
            {
                "Text": "中国台北",
                "Value": "ap-taipei"
            },
            {
                "Text": "武汉EC",
                "Value": "ap-wuhan-ec"
            }
        ],
        "RequestId": "97e5fd5b-67c2-4979-86c9-1469136441c3",
        "Total": 524,
        "VpcList": [
            {
                "Text": "xuann",
                "Value": "vpc-cwcsulhn"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-1hhbcwsu"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-iyn6tg27"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-guv4i1h5"
            },
            {
                "Text": "test_tcs",
                "Value": "vpc-mbgoxtov"
            },
            {
                "Text": "leiting-ddos灰度",
                "Value": "vpc-35utyd61"
            }
        ]
    }
}
```

