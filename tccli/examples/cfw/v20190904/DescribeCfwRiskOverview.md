**Example 1: 查询风险概览**

不传时间时默认查询最近 7 天；total_unhandled_risks 等于 breakdown 五类未处理风险之和。

Input: 

```
tccli cfw DescribeCfwRiskOverview --cli-unfold-argument  \
    --StartTime 2026-06-01 00:00:00 \
    --EndTime 2026-06-02 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": "{\"start_time\":\"2026-06-01 00:00:00\",\"end_time\":\"2026-06-02 00:00:00\",\"total_unhandled_risks\":5,\"breakdown\":{\"data_leak_total\":1,\"data_leak_out_total\":1,\"data_leak_ai_instance_total\":1,\"port_risk_total\":1,\"weak_password_total\":1}}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

