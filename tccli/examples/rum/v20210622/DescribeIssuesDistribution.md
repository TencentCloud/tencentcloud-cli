**Example 1: 拉取统计分布数据**



Input: 

```
tccli rum DescribeIssuesDistribution --cli-unfold-argument  \
    --ProductId 5d4fa0e8d8 \
    --Dimension bundle_id \
    --IssueType 1 \
    --MetricType 1 \
    --RequestHeader BEGIN{"X-ProductId": "5d4fa0e8d8"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"distributions\":[{\"field\":\"com.example.sdkapp\",\"value\":47,\"device_uv\":0,\"user_uv\":0,\"lag_time_cost_avg\":0,\"lag_time_cost_p50\":0,\"lag_time_cost_p75\":0,\"lag_time_cost_p90\":0,\"lag_time_cost_p99\":0,\"http_succ_rate\":0,\"http_conn_rate\":0,\"http_err_count\":\"0\",\"http_total_cost_p50\":0,\"http_dns_cost_p50\":0,\"http_tcp_cost_p50\":0,\"http_ssl_cost_p50\":0,\"http_req_cost_p50\":0,\"http_wait_cost_p50\":0,\"http_res_cost_p50\":0,\"http_first_package_cost_p50\":0,\"http_req_size_p50\":0,\"http_res_size_p50\":0,\"issue_count\":\"0\",\"lag_report_rate\":0,\"lag_device_rate\":0,\"lag_user_rate\":0},{\"field\":\"com.tencent.bugly\",\"value\":6,\"device_uv\":0,\"user_uv\":0,\"lag_time_cost_avg\":0,\"lag_time_cost_p50\":0,\"lag_time_cost_p75\":0,\"lag_time_cost_p90\":0,\"lag_time_cost_p99\":0,\"http_succ_rate\":0,\"http_conn_rate\":0,\"http_err_count\":\"0\",\"http_total_cost_p50\":0,\"http_dns_cost_p50\":0,\"http_tcp_cost_p50\":0,\"http_ssl_cost_p50\":0,\"http_req_cost_p50\":0,\"http_wait_cost_p50\":0,\"http_res_cost_p50\":0,\"http_first_package_cost_p50\":0,\"http_req_size_p50\":0,\"http_res_size_p50\":0,\"issue_count\":\"0\",\"lag_report_rate\":0,\"lag_device_rate\":0,\"lag_user_rate\":0}],\"valid_reported_count\":\"53\",\"valid_device_uv\":\"4\",\"valid_user_uv\":\"11\"}",
        "Message": "",
        "RequestId": "c022ad6a-e994-411c-bd4c-40c3b9d1aab8"
    }
}
```

