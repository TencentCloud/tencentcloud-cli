**Example 1: 查询加固策略信息**



Input: 

```
tccli ms DescribeShieldPlanInstance --cli-unfold-argument  \
    --ResourceId xxx \
    --Pid 1
```

Output: 
```
{
    "Response": {
        "BindInfo": {
            "AppPkgName": "xx",
            "AppIconUrl": "xx",
            "AppName": "xx"
        },
        "ResourceServiceInfo": {
            "ExpireTime": 1,
            "ResourceName": "xx",
            "CreateTime": 1
        },
        "ShieldPlanInfo": {
            "TotalCount": 1,
            "PlanSet": [
                {
                    "PlanName": "xx",
                    "PlanId": 1,
                    "PlanInfo": {
                        "Dex": 1,
                        "SoType": [
                            "so_low_com_dump_huidu"
                        ],
                        "AntiLogLeak": 1,
                        "ApkSizeOpt": 1,
                        "SoInfo": {
                            "SoFileNames": [
                                "1.so",
                                "2.so"
                            ]
                        },
                        "AntiQemuRoot": 1,
                        "AntiVMP": 1,
                        "Db": 1,
                        "SeperateDex": 1,
                        "AntiScreenshot": 1,
                        "So": 1,
                        "AntiRepack": 1,
                        "AntiAssets": 1,
                        "DexSig": 1,
                        "Bugly": 1,
                        "AntiSSL": 1
                    },
                    "IsDefault": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

