**Example 1: foom 个例列表**



Input: 

```
tccli rum DescribeFOOMReportList --cli-unfold-argument  \
    --ProductId 0dc5283a55 \
    --Feature 2556EFA7AF2E1E46D40397C7447BCA48 \
    --PageNumber 1 \
    --PageSize 20 \
    --SortField event_time \
    --SortType DESC \
    --RequestHeader BEGIN{"X-ProductId": "0dc5283a55","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"report_info\":[{\"account_id\":\"f3bf8176ee736908f8974f5500001fa15b0e\",\"report_time\":\"1746605418\",\"client_identify\":\"CDBD416C-17E3-45CB-857A-FBDE7E346BBA\",\"max_malloc_size\":260,\"used_mem\":1127.93,\"os_version\":\"Version 15.6.1 (Build 19G82)\",\"model\":\"iPhone12,1\",\"feature\":\"2556EFA7AF2E1E46D40397C7447BCA48\",\"event_time\":\"1746605418\",\"qimei\":\"f3bf8176ee736908f8974f5500001fa15b0e\",\"app_version\":\"8.9.60.25971\",\"linkages\":[]},{\"account_id\":\"D1DC5812-A484-47F6-B0A4-9FEAB91CF3D1\",\"report_time\":\"1746460178\",\"client_identify\":\"F0D79552-6951-457A-9714-4D801D032D3F\",\"max_malloc_size\":3994.66,\"used_mem\":2425.1,\"os_version\":\"Version 16.4.1 (Build 20E252)\",\"model\":\"iPhone14,2\",\"feature\":\"2556EFA7AF2E1E46D40397C7447BCA48\",\"event_time\":\"1746460178\",\"qimei\":\"D1DC5812-A484-47F6-B0A4-9FEAB91CF3D1\",\"app_version\":\"8.9.60.25971\",\"linkages\":[]},{\"account_id\":\"646EBEC4-46A3-426C-A028-D08306895223\",\"report_time\":\"1746241203\",\"client_identify\":\"3F061F4C-F3C4-4C0B-B008-21D54D972CB1\",\"max_malloc_size\":2458.22,\"used_mem\":2037.3,\"os_version\":\"Version 14.6 (Build 18F72)\",\"model\":\"iPhone12,5\",\"feature\":\"2556EFA7AF2E1E46D40397C7447BCA48\",\"event_time\":\"1746241203\",\"qimei\":\"646EBEC4-46A3-426C-A028-D08306895223\",\"app_version\":\"8.9.60.25971\",\"linkages\":[]},{\"account_id\":\"c2e1e38b80575b15031ba454000010816502\",\"report_time\":\"1744811557\",\"client_identify\":\"894F0423-41B2-4F8E-A4E3-B797FAA50801\",\"max_malloc_size\":256,\"used_mem\":1963.77,\"os_version\":\"Version 16.7.10 (Build 20H350)\",\"model\":\"iPhone10,2\",\"feature\":\"2556EFA7AF2E1E46D40397C7447BCA48\",\"event_time\":\"1744811557\",\"qimei\":\"c2e1e38b80575b15031ba454000010816502\",\"app_version\":\"8.9.60.25971\",\"linkages\":[]},{\"account_id\":\"7e13f4945b098e7f38bdb296000010d15b17\",\"report_time\":\"1744213588\",\"client_identify\":\"CCD32615-BC6C-4821-B1B9-2C761F3AE3C9\",\"max_malloc_size\":3233.78,\"used_mem\":3028.15,\"os_version\":\"Version 15.1 (Build 19B74)\",\"model\":\"iPhone14,2\",\"feature\":\"2556EFA7AF2E1E46D40397C7447BCA48\",\"event_time\":\"1744213588\",\"qimei\":\"7e13f4945b098e7f38bdb296000010d15b17\",\"app_version\":\"8.9.60.25971\",\"linkages\":[]},{\"account_id\":\"e7bedbf43f9232e69cdc343300001a51790c\",\"report_time\":\"1742725452\",\"client_identify\":\"C8428D35-AB99-4A00-AAEF-E900978501D5\",\"max_malloc_size\":260.38,\"used_mem\":864.55,\"os_version\":\"Version 16.6 (Build 20G75)\",\"model\":\"iPhone10,3\",\"feature\":\"2556EFA7AF2E1E46D40397C7447BCA48\",\"event_time\":\"1742725451\",\"qimei\":\"e7bedbf43f9232e69cdc343300001a51790c\",\"app_version\":\"8.9.60.25971\",\"linkages\":[]},{\"account_id\":\"a448e76280d00aeceea5de1c000018a1610b\",\"report_time\":\"1742303878\",\"client_identify\":\"5C61C961-1C9C-4DD1-BA13-3ACBD275C962\",\"max_malloc_size\":1985.5,\"used_mem\":2093.02,\"os_version\":\"Version 17.7 (Build 21H16)\",\"model\":\"iPhone14,5\",\"feature\":\"2556EFA7AF2E1E46D40397C7447BCA48\",\"event_time\":\"1742303878\",\"qimei\":\"a448e76280d00aeceea5de1c000018a1610b\",\"app_version\":\"8.9.60.25971\",\"linkages\":[]}],\"key_methods\":\"[\\\"Foundation -[NSBlockOperation main] +  104\\\",\\\"Foundation ___NSBLOCKOPERATION_IS_CALLING_OUT_TO_A_BLOCK__ +  24\\\",\\\"live4iphoneRel 0x10b6780c8 + 149045448\\\"]\",\"tapd_status\":\"unassigned\",\"tapd_url\":\"\",\"tapd_handler\":\"\",\"issue_status\":\"notRepaired\",\"doc_count\":\"7\",\"qimei_count\":\"7\",\"min_app_version_in_filter\":\"\",\"max_app_version_in_filter\":\"\",\"tags_in_filter\":[],\"notes\":[]}",
        "Message": "",
        "RequestId": "d94051af-143a-48b3-8cf9-6b54059cdad2"
    }
}
```

