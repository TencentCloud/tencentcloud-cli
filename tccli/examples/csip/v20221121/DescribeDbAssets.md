**Example 1: 数据库资产列表查询**



Input: 

```
tccli csip DescribeDbAssets --cli-unfold-argument  \
    --Filter.Filters.0.Name Status \
    --Filter.Filters.0.Values 1 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Filters.1.Name TimeRange \
    --Filter.Filters.1.Values 2 \
    --Filter.Filters.1.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By AssetCreateTime \
    --MemberId mem-625225cc0913c901
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "130215132961",
                "Value": "130215132961"
            }
        ],
        "AssetTypeList": [
            {
                "Text": "MySQL",
                "Value": "MYSQL"
            },
            {
                "Text": "PostgreSQL",
                "Value": "POSTGRES"
            },
            {
                "Text": "MariaDB",
                "Value": "MARIADB"
            }
        ],
        "Data": [
            {
                "AssetId": "postgres-n3rvf26b",
                "AssetType": "POSTGRES",
                "Region": "ap-guangzhou",
                "VpcName": "li-用完删",
                "ConfigurationRisk": 1,
                "AssetName": "Unnamed",
                "VpcId": "vpc-ewf1aiej",
                "Domain": "example.foo2.com",
                "AssetCreateTime": "2024-01-30 16:17:21",
                "LastScanTime": "2024-10-30 05:02:29",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 28,
                "AppId": 130215132961,
                "Uin": "10001459297899",
                "NickName": "声声乌龙2",
                "Port": 0,
                "Tag": [
                    {
                        "Name": "new",
                        "Value": "sign"
                    },
                    {
                        "Name": "业务测试",
                        "Value": "业务测试数据"
                    }
                ],
                "PrivateIp": "192.168.222.101:5432",
                "PublicIp": "1.1.1.1",
                "Status": 1,
                "IsCore": 2,
                "IsNewAsset": 0
            },
            {
                "AssetId": "tdsql-kfbdnfy9",
                "AssetType": "MARIADB",
                "Region": "ap-guangzhou",
                "VpcName": "li-用完删",
                "ConfigurationRisk": 1,
                "AssetName": "tdsql-kfbdnfy9",
                "VpcId": "vpc-ewf1aiej",
                "Domain": "example.foo.com",
                "AssetCreateTime": "2024-01-30 16:12:58",
                "LastScanTime": "2024-10-30 05:02:29",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 28,
                "AppId": 130215132961,
                "Uin": "10001459297899",
                "NickName": "声声乌龙2",
                "Port": 0,
                "Tag": [
                    {
                        "Name": "new",
                        "Value": "sign"
                    }
                ],
                "PrivateIp": "192.168.222.104:3306",
                "PublicIp": "1.1.1.1",
                "Status": 1,
                "IsCore": 2,
                "IsNewAsset": 0
            },
            {
                "AssetId": "cdb-4dckmpb7",
                "AssetType": "MYSQL",
                "Region": "ap-guangzhou",
                "VpcName": "li-用完删",
                "ConfigurationRisk": 5,
                "AssetName": "cdb419972",
                "VpcId": "vpc-ewf1aiej",
                "Domain": "example.foo1.com",
                "AssetCreateTime": "2024-01-30 15:45:08",
                "LastScanTime": "2024-10-30 05:02:29",
                "Attack": 0,
                "Access": 0,
                "ScanTask": 28,
                "AppId": 130215132961,
                "Uin": "10001459297899",
                "NickName": "声声乌龙2",
                "Port": 0,
                "Tag": [
                    {
                        "Name": "new",
                        "Value": "sign"
                    }
                ],
                "PrivateIp": "192.168.222.103:3306",
                "PublicIp": "1.1.1.1",
                "Status": 1,
                "IsCore": 2,
                "IsNewAsset": 0
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
                "Text": "广州",
                "Value": "ap-guangzhou"
            }
        ],
        "RequestId": "1eca062f-ccb9-44c4-b43c-eda42b62607e",
        "Total": 3,
        "VpcList": [
            {
                "Text": "Default-VPC",
                "Value": "vpc-ommo5hlv"
            },
            {
                "Text": "li-用完删",
                "Value": "vpc-ewf1aiej"
            },
            {
                "Text": "fengqqian2",
                "Value": "vpc-fw2ndu5f"
            }
        ]
    }
}
```

