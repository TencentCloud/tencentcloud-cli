**Example 1: 获取套餐**

获取套餐

Input: 

```
tccli tcb DescribeBaasPackageList --cli-unfold-argument  \
    --Source miniapp
```

Output: 
```
{
    "Response": {
        "PackageList": [
            {
                "PackageName": "personal_calculation",
                "PackageTitle": "个人版-计算型",
                "GroupName": "calculation",
                "GroupTitle": "套餐分组中文名",
                "BillTags": "{\"pid\":0, \"cids\":{\"create\":0, \"renew\":0, \"modify\":0}, \"productCode\":0, \"subProductCode\":0}",
                "ResourceLimit": "{\"Capacity\":{\"TimeUnit\":\"m\", \"Unit\":\"GB\", \"MaxSize\": 100}, \"Flux\":{\"TimeUnit\":\"m\", \"Unit\":\"GB\", \"MaxSize\": 100}, \"CalculationTime\":{\"TimeUnit\":\"m\", \"Unit\":\"s\", \"MaxSize\": 100}, \"InvokeNum\":{\"TimeUnit\":\"m\", \"Unit\":\"次\", \"MaxSize\": 100}}",
                "AdvanceLimit": "{\"CMSEnable\":false,\"ProvisionedConcurrencyMem\":512000, \"PictureProcessing\":false, \"SecurityAudit\":false, \"RealTimePush\":false, \"TemplateMessageBatchPush\":false, \"Payment\":false}",
                "PackageDescription": "xxx",
                "IsExternal": true
            }
        ],
        "RequestId": "2e992b19-7906-44a4-a8bb-5a71672b0ec9"
    }
}
```

