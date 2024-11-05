**Example 1: 新增加固策略**



Input: 

```
tccli ms CreateShieldPlanInstance --cli-unfold-argument  \
    --PlanName 默认加固策略 \
    --ResourceId 127500-shi \
    --PlanInfo.AntiRoot 0 \
    --PlanInfo.FileSign 0 \
    --PlanInfo.SetFile 0 \
    --PlanInfo.Dex 1 \
    --PlanInfo.SoType 1 \
    --PlanInfo.AntiLogLeak 0 \
    --PlanInfo.ApkSizeOpt 1 \
    --PlanInfo.SoInfo.SoFileNames a.so \
    --PlanInfo.AntiQemuRoot 0 \
    --PlanInfo.AntiVMP 0 \
    --PlanInfo.Db 0 \
    --PlanInfo.SeperateDex 0 \
    --PlanInfo.AntiScreenshot 0 \
    --PlanInfo.So 1 \
    --PlanInfo.AntiRepack 1 \
    --PlanInfo.AntiAssets 0 \
    --PlanInfo.DexSig 1 \
    --PlanInfo.Bugly 0 \
    --PlanInfo.AntiSSL 0
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

