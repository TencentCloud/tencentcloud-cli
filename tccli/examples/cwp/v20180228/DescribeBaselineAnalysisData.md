**Example 1: 安全基线策略概览统计数据查询接口**

根据基线策略id查询基线策略数据概览统计

Input: 

```
tccli cwp DescribeBaselineAnalysisData --cli-unfold-argument  \
    --StrategyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "LatestScanTime": "最近基线检测时间",
        "IsGlobal": "扫描范围是否全部服务器",
        "ScanHostCount": 170,
        "ScanRuleCount": 25,
        "IfFirstScan": 1
    }
}
```

