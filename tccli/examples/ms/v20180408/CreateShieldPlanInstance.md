**Example 1: 新增加固策略**



Input: 

```
tccli ms CreateShieldPlanInstance --cli-unfold-argument  \
    --PlanName xx \
    --ResourceId xx \
    --PlanInfo.Dex 1 \
    --PlanInfo.SoType xx \
    --PlanInfo.AntiLogLeak 0 \
    --PlanInfo.ApkSizeOpt 1 \
    --PlanInfo.SoInfo.SoFileNames xx \
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

