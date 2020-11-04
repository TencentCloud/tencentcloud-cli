**Example 1: 新增加固策略**



Input: 

```
tccli ms CreateShieldPlanInstance --cli-unfold-argument  \
    --ResourceId 127500-shi\
    --PlanName 默认加固策略\
    --PlanInfo.ApkSizeOpt 1\
    --PlanInfo.Dex 1\
    --PlanInfo.So 1\
    --PlanInfo.Bugly 0\
    --PlanInfo.AntiRepack 1\
    --PlanInfo.Db 0\
    --PlanInfo.DexSig 1\
    --PlanInfo.SeperateDex 0\
    --PlanInfo.AntiLogLeak 0\
    --PlanInfo.AntiVMP 0\
    --PlanInfo.AntiQemuRoot 0\
    --PlanInfo.AntiAssets 0\
    --PlanInfo.AntiScreenshot 0\
    --PlanInfo.AntiSSL 0\
    --PlanInfo.SoType so_low_com_dump_huidu\
    --PlanInfo.SoInfo.SoFileNames 1.so
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Progress": 1,
        "PlanId": 1
    }
}
```

