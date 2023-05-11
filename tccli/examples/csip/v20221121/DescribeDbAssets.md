**Example 1: 接口示例**

接口示例

Input: 

```
tccli csip DescribeDbAssets --cli-unfold-argument ```

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
                "Text": "MySQL",
                "Value": "MYSQL"
            },
            {
                "Text": "CKafka",
                "Value": "KAFKA"
            },
            {
                "Text": "MongoDB",
                "Value": "MONGODB"
            }
        ],
        "Data": [
            {
                "AssetId": "cdb-nbq22l65",
                "AssetName": "cdb379810",
                "AssetType": "MYSQL",
                "VpcId": "vpc-ds7fl5xn",
                "VpcName": "illnggao-test01",
                "Region": "ap-guangzhou",
                "Domain": "",
                "AssetCreateTime": "2023-01-18 09:42:24",
                "LastScanTime": "2023-02-01 15:43:45",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 3,
                "AppId": 1300448058,
                "Uin": "100011616646",
                "NickName": "天空之蓝-现网",
                "Port": 0,
                "Tag": null,
                "PrivateIp": "192.168.1.11:3306",
                "PublicIp": "",
                "Status": 1,
                "ConfigurationRisk": 0
            },
            {
                "AssetId": "ckafka-5k7va8zv",
                "AssetName": "未命名",
                "AssetType": "KAFKA",
                "VpcId": "vpc-imk763v1",
                "VpcName": "Default-VPC",
                "Region": "ap-guangzhou",
                "Domain": "",
                "AssetCreateTime": "2023-01-30 18:29:44",
                "LastScanTime": "2023-02-01 15:43:45",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 2,
                "AppId": 1300448058,
                "Uin": "100011616646",
                "NickName": "天空之蓝-现网",
                "Port": 0,
                "Tag": null,
                "PrivateIp": "172.16.64.4:9092",
                "PublicIp": "",
                "Status": 1,
                "ConfigurationRisk": 0
            },
            {
                "AssetId": "cmgo-prgxqi85",
                "AssetName": "11",
                "AssetType": "MONGODB",
                "VpcId": "vpc-9qn7jrvs",
                "VpcName": "安全组性能vpc",
                "Region": "ap-shanghai",
                "Domain": "",
                "AssetCreateTime": "2022-12-08 17:24:57",
                "LastScanTime": "2023-02-02 11:42:10",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 10,
                "AppId": 1300448058,
                "Uin": "100011616646",
                "NickName": "天空之蓝-现网",
                "Port": 0,
                "Tag": null,
                "PrivateIp": "192.168.2.205;192.168.2.120;192.168.1.189:27017",
                "PublicIp": "",
                "Status": 1,
                "ConfigurationRisk": 0
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
            }
        ],
        "RequestId": "ddec8747-5f31-4eec-9343-ef7fc337fa4f",
        "Total": 3,
        "VpcList": [
            {
                "Text": "illnggao-test01",
                "Value": "vpc-ds7fl5xn"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-imk763v1"
            },
            {
                "Text": "安全组性能vpc",
                "Value": "vpc-9qn7jrvs"
            }
        ]
    }
}
```

