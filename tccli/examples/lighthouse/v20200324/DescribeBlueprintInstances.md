**Example 1: 查询镜像实例信息**



Input: 

```
tccli lighthouse DescribeBlueprintInstances --cli-unfold-argument  \
    --InstanceIds lhins-f4s49nap
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BlueprintInstanceSet": [
            {
                "InstanceId": "lhins-f4s49nap",
                "Blueprint": {
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
                    "CreatedTime": "2024-05-08T03:43:06Z"
                },
                "SoftwareSet": [
                    {
                        "Name": "宝塔Linux面板",
                        "Version": "8.1.0 腾讯云专享版",
                        "ImageUrl": "https://imgcache.qq.com/open_proj/proj_qcloud_v2/tc-console/tea-static-lighthouse/src/styles/slice/bt-panel.svg",
                        "InstallDir": "/www",
                        "DetailSet": [
                            {
                                "Key": "BTPanelIndexUrl",
                                "Title": "面板首页地址",
                                "Value": "http://1.13.251.147:面板端口/tencentcloud"
                            },
                            {
                                "Key": "BTPanelPort",
                                "Title": "面板端口",
                                "Value": "默认为8888，您可以在登录面板后修改面板端口"
                            },
                            {
                                "Key": "BTPanelCredential",
                                "Title": "用户名与密码",
                                "Value": "sudo /etc/init.d/bt default"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "128d0517-4eb0-4301-868c-650eaeac5556"
    }
}
```

