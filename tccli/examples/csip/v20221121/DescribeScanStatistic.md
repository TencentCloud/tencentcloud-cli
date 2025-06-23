**Example 1: 查询暴露面扫描结果统计信息**

查询暴露面扫描结果统计信息

Input: 

```
tccli csip DescribeScanStatistic --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "HighRiskPortServiceCount": 3,
        "PortServiceCount": 3,
        "PortServiceIncrement": 0,
        "RequestId": "45ca21d4-f373-4274-9295-5380abc74bed",
        "RiskWebAppCount": 0,
        "VulCount": 0,
        "WeakPasswordCount": 1,
        "WebAppCount": 0,
        "WebAppIncrement": 0
    }
}
```

