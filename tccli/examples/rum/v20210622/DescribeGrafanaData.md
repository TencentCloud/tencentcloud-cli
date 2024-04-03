**Example 1: 11**



Input: 

```
tccli rum DescribeGrafanaData --cli-unfold-argument  \
    --Query U0hPVyBNRUFTVVJFTUVOVFMgTElNSVQgMTAw
```

Output: 
```
{
    "Response": {
        "RequestId": "c762c7dc-c42a-4e40-9090-82b079b982aa",
        "Result": "{\"request_id\":\"5cdde60cf37352dc647cceb4-1805ea023f7\",\"results\":[{\"statement_id\":0,\"series\":[{\"name\":\"measurements\",\"columns\":[\"name\"],\"values\":[[\"custom_url_info\"],[\"custom_url_statistics\"],[\"dau_project_unique\"],[\"dau_user_event_unique\"],[\"event_url_info\"],[\"event_url_statistics\"],[\"fetch_project_statistics\"],[\"fetch_status_error_count\"],[\"fetch_url_info\"],[\"fetch_url_statistics\"],[\"log_url_info\"],[\"log_url_statistics\"],[\"mau_project_unique\"],[\"performance_page_statistics\"],[\"performance_project_statistics\"],[\"pv_url_info\"],[\"pv_url_statistics\"],[\"report_count\"],[\"set_data_url_statistics\"],[\"static_project_statistics\"],[\"static_resource_statistics\"],[\"static_status_error_count\"],[\"static_url_source\"],[\"tccm_client_internal_metrics\"],[\"telegraf_agent\"],[\"telegraf_gather\"],[\"telegraf_statsd\"],[\"telegraf_write\"],[\"user_event_user_event_unique\"],[\"uv_page_unique\"],[\"uv_project_unique\"],[\"wau_project_unique\"],[\"webvitals_page_statistics\"],[\"webvitals_project_statistics\"]]}],\"total\":0}]}"
    }
}
```

**Example 2: DescribeGrafanaData**



Input: 

```
tccli rum DescribeGrafanaData --cli-unfold-argument  \
    --Query select
```

Output: 
```
{
    "Response": {
        "Result": "xxxx",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

