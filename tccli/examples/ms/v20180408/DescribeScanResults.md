**Example 1: 查询扫描结果**

通过唯一标识获取加固的结果，唯一标识ItemId通过请求扫描接口返回

Input: 

```
tccli ms DescribeScanResults --cli-unfold-argument  \
    --ItemId 1shi2e-2387hjgus \
    --AppMd5s dd5b29a800246d7089febf228286d901
```

Output: 
```
{
    "Response": {
        "RequestId": "8fdbd2b2-2867-4758-b450-5bac2d37440f",
        "ScanSet": [
            {
                "AdInfo": {
                    "Banners": [],
                    "BoutiqueRecommands": [],
                    "FloatWindowses": [],
                    "IntegralWalls": [],
                    "NotifyBars": [],
                    "Spots": []
                },
                "AppDetailInfo": {
                    "AppIconUrl": "http://ms-shield-1251001047.cos.ap-guangzhou.myqcloud.com/legu_icon/1255750086/a9d5f689b518beccc54a6f4286d18bcd?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDmQtAxYTAB2iBS8s2DCzazCD2g7OUq4Zw%26q-sign-time%3D1524646732%3B1524647092%26q-key-time%3D1524646732%3B1524647092%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Da8553d5e3c61c2a44f16e9949b409b94d553d3e0%00",
                    "AppMd5": "bc80057cf4323db8579e011f8a5f1402",
                    "AppName": "",
                    "AppPkgName": "",
                    "AppSize": 484980,
                    "AppVersion": "",
                    "FileName": "testname"
                },
                "PermissionInfo": {
                    "PermissionList": [
                        {
                            "Permission": "android.permission.READ_EXTERNAL_STORAGE"
                        },
                        {
                            "Permission": "android.permission.WRITE_EXTERNAL_STORAGE"
                        },
                        {
                            "Permission": "android.permission.INTERNET"
                        }
                    ]
                },
                "SensitiveInfo": {
                    "SensitiveList": [
                        {
                            "FilePath": "0000bbd2fdef20ad2fa7caef1a9f1e762532f78c/resources.arsc",
                            "FileSha": "3513b0e608e075f2e1beb49ba32d59b3e44d7622",
                            "WordList": [
                                "手槍"
                            ]
                        }
                    ]
                },
                "StatusCode": 0,
                "StatusDesc": "",
                "StatusRef": "",
                "TaskStatus": 1,
                "TaskTime": 1546511829,
                "VirusInfo": {
                    "SafeType": 1,
                    "VirusDesc": "",
                    "VirusName": ""
                },
                "VulInfo": {
                    "VulFileScore": 0,
                    "VulList": [
                        {
                            "RiskLevel": 1,
                            "VulCode": "<com.unity3d.player.UnityPlayer: void <init>(android.content.ContextWrapper)>",
                            "VulDesc": "在android中使用Broadcast接收广播的过程中，当receiver没有进行合适的配置时，可能导致攻击者构造广播发送给被攻击recevier。导致被攻击应用接受到错误信息，从而导致进一步的危害。",
                            "VulFilepath": "classes.dex",
                            "VulId": "22",
                            "VulName": "Broadcast Receiver组件暴露风险（含动态注册）",
                            "VulSolution": "1.如果应用的Receiver组件不必要导出，或者组件配置了intent filter标签，建议在AndroidManifest.xml文件中设置组件的“android:exported”属性为false\n2.如果组件必须要提供给外部应用使用，建议对组件进行权限控制",
                            "VulSrcType": 1
                        },
                        {
                            "RiskLevel": 2,
                            "VulCode": "debuggable option do not disable in AndroidManifest",
                            "VulDesc": "在AndroidManifest.xml中配置debuggable=true导致程序可以被调试，有数据泄漏的风险",
                            "VulFilepath": "AndroidManifest.xml",
                            "VulId": "1",
                            "VulName": "调试标志未关闭漏洞",
                            "VulSolution": "在AndroidManifest.xml配置debuggable=false",
                            "VulSrcType": 0
                        },
                        {
                            "RiskLevel": 2,
                            "VulCode": "allowBackUp option do not disable in AndroidManifest",
                            "VulDesc": "在AndroidManifest.xml若将allowBackUp属性设为true，用户即可通过adb buckup命令备份文件数据并通过adb restore命令将备份文件导入",
                            "VulFilepath": "AndroidManifest.xml",
                            "VulId": "2",
                            "VulName": "allowBackUp文件备份漏洞",
                            "VulSolution": "在应用正式发布之前将AndroidManifest.xml文件中的allowBackUp属性值设置为false",
                            "VulSrcType": 0
                        }
                    ]
                }
            }
        ],
        "TotalCount": 1
    }
}
```

