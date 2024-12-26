**Example 1: 空示例**

空示例

Input: 

```
tccli csip DescribeClusterAssets --cli-unfold-argument  \
    --Filter.Filters.0.Name TimeRange \
    --Filter.Filters.0.Values 2 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By InstanceCreateTime \
    --MemberId mem-b21i4hgxa
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1300448058",
                "Value": "1300448058"
            },
            {
                "Text": "1302396215",
                "Value": "1302396215"
            },
            {
                "Text": "1305350016",
                "Value": "1305350016"
            }
        ],
        "ClusterStatusList": [
            {
                "Text": "运行中",
                "Value": "running"
            }
        ],
        "ClusterTypeList": [
            {
                "Text": "托管集群",
                "Value": "managed_cluster"
            },
            {
                "Text": "弹性集群",
                "Value": "eks"
            }
        ],
        "ComponentStatusList": [
            {
                "Text": "未安装",
                "Value": "defender_uninstall"
            }
        ],
        "Data": [
            {
                "AppId": 1302396215,
                "AssetId": "cls-bc1916ky",
                "AssetName": "benben",
                "AssetType": "managed_cluster",
                "Region": "ap-guangzhou",
                "ServiceCount": 17,
                "PodCount": 41,
                "MachineCount": 1,
                "VpcId": "vpc-fw2ndu5f",
                "KubernetesVersion": "1.30.0",
                "Component": "containerd",
                "CheckCount": 43,
                "VulRisk": 0,
                "CFGRisk": 1,
                "InstanceCreateTime": "2024-12-04 10:33:08",
                "Status": "running",
                "ComponentStatus": "defended",
                "Uin": "100014592178",
                "VpcName": "fengqqian2test",
                "CheckTime": "",
                "ComponentVersion": "1.6.9",
                "Nick": "声声乌龙",
                "IsCore": 1,
                "IsNewAsset": 0,
                "ProtectStatus": 0,
                "ProtectInfo": "AccessedSubNone",
                "CloudType": 0
            }
        ],
        "ProtectStatusList": [
            {
                "Text": "未接入",
                "Value": "0"
            },
            {
                "Text": "未防护",
                "Value": "1"
            },
            {
                "Text": "部分防护",
                "Value": "2"
            },
            {
                "Text": "防护中",
                "Value": "3"
            },
            {
                "Text": "接入异常",
                "Value": "4"
            },
            {
                "Text": "接入中",
                "Value": "5"
            },
            {
                "Text": "卸载中",
                "Value": "6"
            },
            {
                "Text": "卸载异常",
                "Value": "7"
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            }
        ],
        "RequestId": "035c9d95-a2da-465e-b735-535d9afed6cf",
        "TotalCount": 1,
        "VpcList": [
            {
                "Text": "wy conflict",
                "Value": "vpc-39sc6ru5"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-ommo5hlv"
            },
            {
                "Text": "fengqqian2test",
                "Value": "vpc-fw2ndu5f"
            },
            {
                "Text": "gordan-test1",
                "Value": "vpc-q1of50wz"
            }
        ]
    }
}
```

