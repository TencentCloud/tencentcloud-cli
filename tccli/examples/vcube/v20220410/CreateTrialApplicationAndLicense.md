**Example 1: 创建测试应用并开通测试 license**

创建测试应用并开通测试 license

Input: 

```
tccli vcube CreateTrialApplicationAndLicense --cli-unfold-argument  \
    --AppName QQ \
    --BundleId com.company.appName \
    --PackageName com.company.appName \
    --FeatureIds 3 16 \
    --PlanList S1-04
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

