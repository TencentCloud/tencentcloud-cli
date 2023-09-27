**Example 1: 所有db资产示例**

所有db资产示例

Input: 

```
tccli csip DescribeDbAssets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1300846651",
                "Value": "1300846651"
            }
        ],
        "AssetTypeList": [
            {
                "Text": "COS",
                "Value": "COS"
            },
            {
                "Text": "MySQL",
                "Value": "MYSQL"
            },
            {
                "Text": "CFS",
                "Value": "CFS"
            },
            {
                "Text": "CBS",
                "Value": "CBS"
            }
        ],
        "Data": [
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2023-08-31 19:37:18",
                "AssetId": "cdb-pxwani6r",
                "AssetName": "cdb115086",
                "AssetType": "MYSQL",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 1,
                "IsNewAsset": 0,
                "LastScanTime": "-",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "10.25.25.2:3306",
                "PublicIp": "",
                "Region": "ap-chongqing",
                "ScanTask": 0,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "vpc-h2i9m8xh",
                "VpcName": "fengqqian"
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2023-08-31 10:15:36",
                "AssetId": "disk-51a0diaa",
                "AssetName": "未命名_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "-",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-chongqing",
                "ScanTask": 0,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2020-10-09 16:46:52",
                "AssetId": "disk-jckoxu4h",
                "AssetName": "NAT_VPC autotest,勿删_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "2023-09-04 16:59:17",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-shanghai",
                "ScanTask": 14,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2022-12-05 10:39:35",
                "AssetId": "disk-hq4yircx",
                "AssetName": "数据盘漏扫测试",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "2023-09-04 16:59:17",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-beijing",
                "ScanTask": 14,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2020-10-16 17:30:35",
                "AssetId": "disk-haamhu15",
                "AssetName": "VPC-autotest2,勿删_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "2023-09-04 16:59:17",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-shanghai",
                "ScanTask": 14,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2023-08-31 19:15:48",
                "AssetId": "disk-g3lx4gh0",
                "AssetName": "私有网络广州3区v_tximtantest_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "-",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-guangzhou",
                "ScanTask": 0,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2023-06-30 15:06:08",
                "AssetId": "disk-dh874mht",
                "AssetName": "未命名_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "2023-09-04 16:59:17",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-beijing",
                "ScanTask": 12,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2023-08-30 18:10:46",
                "AssetId": "disk-dcyyxrhk",
                "AssetName": " v_tximtantest_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "-",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-guangzhou",
                "ScanTask": 0,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2020-10-16 17:20:32",
                "AssetId": "disk-d5emuwa3",
                "AssetName": "VPC-autotest,勿删_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "2023-09-04 16:59:17",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-shanghai",
                "ScanTask": 14,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            },
            {
                "Access": 0,
                "AppId": 1300846651,
                "AssetCreateTime": "2020-06-18 17:24:02",
                "AssetId": "disk-8ve9yxot",
                "AssetName": "未命名_系统盘",
                "AssetType": "CBS",
                "Attack": 0,
                "ConfigurationRisk": 0,
                "Domain": "",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "2023-09-04 16:59:17",
                "NickName": "焦糖小蛋糕",
                "Port": 0,
                "PrivateIp": "",
                "PublicIp": "",
                "Region": "ap-shanghai",
                "ScanTask": 14,
                "Status": 1,
                "Tag": null,
                "Uin": "100011949846",
                "VpcId": "",
                "VpcName": ""
            }
        ],
        "RegionList": [
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "重庆",
                "Value": "ap-chongqing"
            },
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "中国香港",
                "Value": "ap-hongkong"
            },
            {
                "Text": "北京",
                "Value": "ap-beijing"
            },
            {
                "Text": "南京",
                "Value": "ap-nanjing"
            }
        ],
        "RequestId": "7899491b-9407-4bca-8363-ddddbbb3486c",
        "Total": 29,
        "VpcList": [
            {
                "Text": "fengqqian",
                "Value": "vpc-h2i9m8xh"
            }
        ]
    }
}
```

