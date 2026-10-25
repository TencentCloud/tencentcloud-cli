**Example 1: 示例**



Input: 

```
tccli rum DescribeIssueEventDetail --cli-unfold-argument  \
    --AppId 146692 \
    --IssueId ca5ac1fb1f4d2993581ea232a73d4575e69579f254f110460c544117ae275fd9 \
    --EventId evt_1781682085980_diyxj1
```

Output: 
```
{
    "Response": {
        "Result": "{\"Data\":{\"event_id\":\"evt_1781682085980_diyxj1\",\"event_time\":1781682085980,\"session_id\":\"663f56e2a6554b959cc7d432b16bcd3f\",\"trace_id\":\"\",\"event_type\":\"promise_error\",\"error_type\":\"Error\",\"error_value\":\"这是一个测试Promise异常\",\"block_duration_ms\":0,\"block_threshold_ms\":0,\"symbolication_status\":\"\",\"crash_thread_id\":\"\",\"stack_trace\":[{\"function\":\"testPromiseError\",\"file\":\"mall-demo.html\",\"line\":818,\"in_app\":true},{\"function\":\"HTMLButtonElement.onclick\",\"file\":\"mall-demo.html\",\"line\":291,\"in_app\":true}],\"context\":{\"app_version\":\"2.0.4\",\"crash_thread_id\":\"\",\"environment\":\"test\",\"error_type\":\"Error\",\"error_value\":\"这是一个测试Promise异常\",\"event_type\":\"promise_error\",\"os\":\"Mac OS X\",\"process_type\":\"\",\"release\":\"2.0.4\",\"session_id\":\"663f56e2a6554b959cc7d432b16bcd3f\",\"symbolication_status\":\"\",\"trace_id\":\"\"}}}",
        "RequestId": "ed98dbb5-a6d9-4067-a64f-4b191548d8fd"
    }
}
```

