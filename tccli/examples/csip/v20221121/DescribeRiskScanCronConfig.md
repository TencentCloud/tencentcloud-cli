**Example 1: 创建用户周期扫描计划**



Input: 

```
tccli csip DescribeRiskScanCronConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CronConfig": {
            "AddRuleEnableStatus": true,
            "CreateAppID": 1302396215,
            "CronStatus": 0,
            "PlanContent": "0 0 16 * * 1,2,**4,5,6,7 *",
            "ScanPlanTimezone": "Asia/Shanghai"
        },
        "RequestId": "687dbdee-2a3e-4668-b3d9-6eac3be03e27"
    }
}
```

