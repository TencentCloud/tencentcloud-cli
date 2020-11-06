**Example 1: 查询加固策略信息**



Input: 

```
tccli ms DescribeShieldPlanInstance --cli-unfold-argument  \
    --Pids 12750 \
    --ResourceId jsihsih-xx
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "BindInfo": {
            "AppIconUrl": "",
            "AppName": "微信",
            "AppPkgName": "com.tencent.mm"
        },
        "ShieldPlanInfo": {
            "TotalCount": 5,
            "PlanSet": [
                {
                    "IsDefault": 0,
                    "PlanId": 1,
                    "PlanName": "部分加固",
                    "PlanInfo": {
                        "ApkSizeopt": 1,
                        "Dex": 1,
                        "So": 1,
                        "Bugly": 1,
                        "AntiRepack": 1,
                        "SeperateDex": 0,
                        "Db": 0,
                        "DexSig": 1,
                        "AntiLogLeak": 0,
                        "AntiVMP": 0,
                        "AntiQemuRoot": 0,
                        "AntiAssets": 0,
                        "AntiScreenshot": 0,
                        "AntiSSL": 0,
                        "SoType": [
                            "so_low_com_dump_huidu"
                        ],
                        "SoInfo": {
                            "SoFileNames": [
                                "1.so",
                                "2.so"
                            ]
                        }
                    }
                }
            ]
        },
        "ResourceServiceInfo": {
            "CreateTime": "",
            "ExpireTime": ""
        }
    }
}
```

