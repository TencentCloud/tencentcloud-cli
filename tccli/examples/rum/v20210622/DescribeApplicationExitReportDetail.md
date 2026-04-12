**Example 1: 进程异常退出个例详情**



Input: 

```
tccli rum DescribeApplicationExitReportDetail --cli-unfold-argument  \
    --ProductId 0dc5283a55 \
    --ClientIdentify 62977F7D-2F27-4273-8E81-F63827C46C36 \
    --StartEventTime 1748174885 \
    --EndEventTime 1748174885 \
    --RequestHeader BEGIN{"X-ProductId": "0dc5283a55","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"problem_detail\":{\"report_time\":\"1748257290\",\"process_name\":\"\",\"app_version\":\"9.01.21.25273\",\"account_id\":\"be3405c1d89c3cc920189519000011a1851f\",\"os_version\":\"Version 17.5.1 (Build 21F90)\",\"qimei\":\"be3405c1d89c3cc920189519000011a1851f\",\"model\":\"iPhone15,5\",\"client_identify\":\"62977F7D-2F27-4273-8E81-F63827C46C36\",\"bundle_id\":\"com.tencent.live4iphone\",\"exit_reason\":24,\"exit_description\":\"\",\"file_path\":\"\",\"file_name\":\"\",\"tombstone\":null,\"anr_trace\":\"\",\"crash_identify\":\"\",\"exit_time\":\"1748174885\",\"issue_uuid\":\"\",\"brand\":\"\",\"hot_patch_version\":\"\",\"vmmap_info\":\"\",\"tick_info\":\"{\\\"last_vc\\\":\\\"QLHomeController\\\",\\\"looper_monitor_tick_last_time\\\":1748174885,\\\"last_app_state\\\":2,\\\"app_state_update_time\\\":1748174626,\\\"app_fg_active_time\\\":1145,\\\"looper_monitor_tick_times\\\":71681,\\\"main_thread_tick_times\\\":73147,\\\"main_thread_tick_last_time\\\":1748174885,\\\"last_enter_fg_time\\\":1748173481,\\\"last_active_time\\\":1748174885}\",\"exit_info\":\"{\\\"signal\\\":0,\\\"exc_code\\\":{\\\"code0\\\":0,\\\"code1\\\":0},\\\"is_deadlock\\\":0,\\\"is_terminate\\\":0,\\\"is_exit\\\":0,\\\"is_crash\\\":0,\\\"exception\\\":0,\\\"cpu_wakeups\\\":{\\\"wakeups_count\\\":224846,\\\"interrupt_wakeups_count\\\":206812,\\\"timer_wakeups_count\\\":16115,\\\"wakeups_duration\\\":278000},\\\"last_update_time\\\":0}\",\"sdk_version\":\"2.8.1-beta.6\",\"vmmaps\":[],\"malloc_zones\":[],\"rom_name\":\"\"}}",
        "Message": "",
        "RequestId": "ee6d8787-d855-4171-ab9c-a58f03ec008f"
    }
}
```

