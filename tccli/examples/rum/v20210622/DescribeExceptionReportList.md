**Example 1: 拉取个例列表**



Input: 

```
tccli rum DescribeExceptionReportList --cli-unfold-argument  \
    --ProductId 5d4fa0e8d8 \
    --IssueType 1 \
    --Feature 6D0914E53B7B0E4CA61005BE48F26D16 \
    --PageSize 1 \
    --PageNumber 1 \
    --RequestHeader BEGIN{"X-ProductId": "5d4fa0e8d8","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"reports\":[{\"feature\":\"6D0914E53B7B0E4CA61005BE48F26D16\",\"client_identify\":\"6e2afeb7-a7d9-4a0d-8046-6bf817a6ed74\",\"app_version\":\"4.4.3-SNAPSHOT\",\"event_time\":\"1745408741\",\"report_time\":\"1745408741\",\"qimei\":\"183ea3d1ed17004f9191cbf9eed40e97\",\"os_version\":\"Android 11,level 30\",\"model\":\"MT2110\",\"type\":\"0\",\"oom_type\":\"\",\"account_id\":\"100000\",\"bundle_id\":\"com.example.sdkapp\",\"rom_name\":\"Oppo/COLOROS/V12\",\"cpu_arch_real\":\"arm64-v8a\",\"is_root\":\"false\",\"free_mem\":\"2619748352\",\"free_sd_card\":\"28985765888\",\"free_storage\":\"28985765888\",\"mem_size\":\"7632023552\",\"total_sd_size\":\"241109250048\",\"total_size\":\"241109250048\",\"crash_time\":\"1745408500\",\"event_time_in_ms\":\"1745408500183\",\"linkages\":[]}],\"key_methods\":\"java.lang.NullPointerException\\ncom.example.test.bugly.BuglyTestActivity.testJavaCrash\\ncom.example.test.bugly.BuglyTestActivity.lambda$onCreate$0\\ncom.example.test.bugly.-$$Lambda$BuglyTestActivity$w4izlE_jhOR7z9BZ_ZcfnlYYmLI.onClick\",\"doc_count\":\"38\",\"qimei_count\":\"2\",\"user_count\":\"0\",\"tapd_status\":\"unassigned\",\"issue_status\":\"notRepaired\",\"notes\":[],\"tapd_url\":\"\",\"tapd_handler\":\"\",\"exception_name\":\"java.lang.NullPointerException\",\"exception_message\":\"Attempt to invoke virtual method 'int java.lang.String.length()' on a null object reference\"}",
        "Message": "",
        "RequestId": "21352396-4421-4d3b-b549-6da749d69fae"
    }
}
```

