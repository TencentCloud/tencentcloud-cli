**Example 1: 查询全流量分析报告数据**

按 full_traffic 场景返回防火墙分析报告数据；示例仅展示一个代表性 section，业务结果在 Response.Data 中。

Input: 

```
tccli cfw DescribeCfwAnalysisData --cli-unfold-argument  \
    --Scenario full_traffic \
    --StartTime 2026-06-01 00:00:00 \
    --EndTime 2026-06-02 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": "{\"status\":\"success\",\"data\":{\"sections\":{\"beacon\":{\"available\":true,\"records\":[{\"src_ip\":\"10.0.0.1\"}]}}},\"metadata\":{\"scenario\":\"full_traffic\"}}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

