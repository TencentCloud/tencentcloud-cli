**Example 1: 仓库镜像列表**

仓库镜像列表

Input: 

```
tccli csip DescribeRepositoryImageAssets --cli-unfold-argument  \
    --Filter.Filters.0.Name TimeRange \
    --Filter.Filters.0.Values 2 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By InstanceCreateTime \
    --MemberId mem-1fc116ccbc8ac7f6
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:2edaeff81ea32d22d88bd7725c7a9fdf6057f8157b45f3bd9d3f75fbf692c187",
                "InstanceName": "sha256:2edaeff81ea32d22d88bd7725c7a9fdf6057f8157b45f3bd9d3f75fbf692c187",
                "InstanceCreateTime": "2024-12-11 10:25:01",
                "RepositoryName": "openobserve",
                "RepositoryUrl": "piper.tencentcloudcr.com/redau/openobserve",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "v0.13.2",
                "InstanceSize": "69.22MB",
                "BuildCount": 5,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:7a1293036d51f6db27889bc5907e3d8264b1c749f0c9d88412bca6004a221148",
                "InstanceName": "sha256:7a1293036d51f6db27889bc5907e3d8264b1c749f0c9d88412bca6004a221148",
                "InstanceCreateTime": "2024-12-10 17:43:13",
                "RepositoryName": "etcd",
                "RepositoryUrl": "piper.tencentcloudcr.com/redau/etcd",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "3.5.11",
                "InstanceSize": "54.17MB",
                "BuildCount": 1,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:89d22e819fbd4f7fb97fe2bfd756993e0a193f66029a3eb8e41f43c42bedfaf7",
                "InstanceName": "sha256:89d22e819fbd4f7fb97fe2bfd756993e0a193f66029a3eb8e41f43c42bedfaf7",
                "InstanceCreateTime": "2024-12-10 17:42:02",
                "RepositoryName": "openresty-waf",
                "RepositoryUrl": "piper.tencentcloudcr.com/redau/openresty-waf",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "latest",
                "InstanceSize": "162.18MB",
                "BuildCount": 10,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:13e1b9e5d6d1d14bb84c6110604ba31bebb5cd0225efd72d943ae9f138d2153c",
                "InstanceName": "sha256:13e1b9e5d6d1d14bb84c6110604ba31bebb5cd0225efd72d943ae9f138d2153c",
                "InstanceCreateTime": "2024-12-09 19:02:20",
                "RepositoryName": "apisix",
                "RepositoryUrl": "piper.tencentcloudcr.com/redau/apisix",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "3.11.0-debian",
                "InstanceSize": "109.72MB",
                "BuildCount": 17,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:d80c3a4e5e0c8112f09b706334d774178f4819d7af0a26425ce982616a03fe22",
                "InstanceName": "sha256:d80c3a4e5e0c8112f09b706334d774178f4819d7af0a26425ce982616a03fe22",
                "InstanceCreateTime": "2024-11-28 15:43:10",
                "RepositoryName": "a_test",
                "RepositoryUrl": "piper.tencentcloudcr.com/tcss/a_test",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "20241128154243",
                "InstanceSize": "2.68MB",
                "BuildCount": 17,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:187e97a2774010c25471303e53657f9c6e379f2b4154c383c42bb5fb24feb5d9",
                "InstanceName": "sha256:187e97a2774010c25471303e53657f9c6e379f2b4154c383c42bb5fb24feb5d9",
                "InstanceCreateTime": "2024-11-27 21:15:38",
                "RepositoryName": "a_test",
                "RepositoryUrl": "piper.tencentcloudcr.com/tcss/a_test",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "20241127211511",
                "InstanceSize": "2.68MB",
                "BuildCount": 17,
                "CheckCount": 6,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:797709008ddc697c8a5ec5075ac91b871f78bd90bbeae8a9dec7c8b369b242a7",
                "InstanceName": "sha256:797709008ddc697c8a5ec5075ac91b871f78bd90bbeae8a9dec7c8b369b242a7",
                "InstanceCreateTime": "2024-11-27 20:20:43",
                "RepositoryName": "a_test",
                "RepositoryUrl": "piper.tencentcloudcr.com/tcss/a_test",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "20241127202016",
                "InstanceSize": "2.68MB",
                "BuildCount": 17,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:1f87a796cb813e82f915f4a58864b9b7ccd544ad007391fd2b6dc722f5805e69",
                "InstanceName": "sha256:1f87a796cb813e82f915f4a58864b9b7ccd544ad007391fd2b6dc722f5805e69",
                "InstanceCreateTime": "2024-11-20 15:01:24",
                "RepositoryName": "tlinux3.1-ttyd-nvim",
                "RepositoryUrl": "piper.tencentcloudcr.com/redau/tlinux3.1-ttyd-nvim",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "v1",
                "InstanceSize": "1.80GB",
                "BuildCount": 16,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:82f6de470fd94cfa6e210541a5d10f8a8bf0b941759afb1239101653e6e451dd",
                "InstanceName": "sha256:82f6de470fd94cfa6e210541a5d10f8a8bf0b941759afb1239101653e6e451dd",
                "InstanceCreateTime": "2024-11-20 14:28:15",
                "RepositoryName": "apereo-cas",
                "RepositoryUrl": "piper.tencentcloudcr.com/redau/apereo-cas",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "4.1.5",
                "InstanceSize": "265.16MB",
                "BuildCount": 31,
                "CheckCount": 6,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            },
            {
                "AppId": 1256299843,
                "Uin": "100004506473",
                "NickName": "飞快的云镜",
                "InstanceId": "sha256:358ff7cbe6c0aa21f7bd99152074f4d951c7a91857c33f4a8c2790261c8ad404",
                "InstanceName": "sha256:358ff7cbe6c0aa21f7bd99152074f4d951c7a91857c33f4a8c2790261c8ad404",
                "InstanceCreateTime": "2024-10-15 17:24:46",
                "RepositoryName": "a_test",
                "RepositoryUrl": "piper.tencentcloudcr.com/tcss/a_test",
                "InstanceType": "TCR镜像",
                "Region": "ap-guangzhou",
                "InstanceVersion": "20241015172428",
                "InstanceSize": "2.68MB",
                "BuildCount": 17,
                "CheckCount": 3,
                "VulRisk": 0,
                "AuthStatus": 0,
                "IsCore": 2,
                "CheckTime": "2025-06-03 20:04:30",
                "IsNewAsset": 0
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "新加坡",
                "Value": "ap-singapore"
            }
        ],
        "RequestId": "a107da68-7b14-48e4-9b1a-8c8688fb7d20",
        "Total": 411
    }
}
```

