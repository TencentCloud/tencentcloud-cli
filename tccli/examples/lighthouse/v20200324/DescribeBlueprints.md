**Example 1: 查询镜像信息**

查询镜像信息

Input: 

```
tccli lighthouse DescribeBlueprints --cli-unfold-argument  \
    --BlueprintIds lhbp-lf6jlx98
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BlueprintSet": [
            {
                "BlueprintId": "lhbp-lf6jlx98",
                "DisplayTitle": "宝塔Linux面板",
                "DisplayVersion": "8.1.0 腾讯云专享版",
                "BlueprintName": "btpanel_exclusive",
                "Description": "宝塔Linux面板（BT-Panel）是一款简单好用的服务器运维管理面板，支持一键LAMP/LNMP/集群/监控/网站/FTP/数据库/JAVA等100多项服务器管理功能，能够极大提升运维管理效率。宝塔面板腾讯云专享版由腾讯云与堡塔公司联合开发，与普通版相比，专享版默认集成腾讯云COSFS、CDN和DNS解析插件，让用户更便捷的使用宝塔面板对腾讯云产品进行管理和操作。该镜像基于OpenCloudOS 9操作系统。",
                "OsName": "OpenCloudOS 9",
                "Platform": "OPENCLOUDOS",
                "PlatformType": "LINUX_UNIX",
                "BlueprintType": "APP_OS",
                "ImageUrl": "https://cloudcache.tencent-cloud.com/open_proj/proj_qcloud_v2/tc-console/tea-static-lighthouse/src/styles/slice/bt-panel.svg",
                "RequiredSystemDiskSize": 20,
                "RequiredMemorySize": 1,
                "BlueprintState": "NORMAL",
                "SupportAutomationTools": true,
                "ImageId": "",
                "CommunityUrl": "https://www.bt.cn",
                "GuideUrl": "https://cloud.tencent.com/document/product/1207/47425",
                "SceneIdSet": [
                    "lhsc-3bzsddow"
                ],
                "DockerVersion": null,
                "BlueprintShared": false,
                "Tags": [],
                "CreatedTime": "2024-05-08T03:43:06Z"
            }
        ],
        "RequestId": "817c4e56-36fc-47ff-bfb6-c4462816972b"
    }
}
```

