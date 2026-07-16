**Example 1: 查询风险概览**

不传时间时默认查询最近 7 天未处理风险概览。

Input: 

```
tccli cfw DescribeCfwRiskOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": "{\"total_unhandled_risks\":1,\"breakdown\":{\"port_risk_total\":1}}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

