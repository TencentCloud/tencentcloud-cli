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

**Example 2: 按目标排查访问阻断**

Target 对该场景全部分析段追加目标过滤；SkipSections 可跳过不需要或已知不可用的分析段。输出仅展示一个代表性 section，实际返回全部未跳过的 section。

Input: 

```
tccli cfw DescribeCfwAnalysisData --cli-unfold-argument  \
    --Scenario access_troubleshoot \
    --Target 10.0.0.1 \
    --SkipSections ips_block
```

Output: 
```
{
    "Response": {
        "Data": "{\"status\":\"success\",\"data\":{\"sections\":{\"acl_border_block\":{\"available\":true,\"records\":[]}}},\"metadata\":{\"scenario\":\"access_troubleshoot\",\"object\":{\"type\":\"user\"}}}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

