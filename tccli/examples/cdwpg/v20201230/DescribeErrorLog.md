**Example 1: 错误日志**

查询错误日志详细信息

Input: 

```
tccli cdwpg DescribeErrorLog --cli-unfold-argument  \
    --InstanceId cdwpg-rzshdeh1 \
    --StartTime 2025-03-01 12:12:12 \
    --EndTime 2025-03-20 12:12:12 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ErrorLogDetails": [
            {
                "Database": "postgres",
                "ErrorMessage": "2025-03-20 12:12:05.850 CST [unknown] 9.0.107.9(48928) postgres tbase 347135 0ERROR:  function fn_stat_get_activity(integer, integer) does not exist at character 278 2025-03-20 12:12:05.850 CST [unknown] 9.0.107.9(48928) postgres tbase 347135 0HINT:  No function matches the given name and argument types. You might need to add explicit type casts. 2025-03-20 12:12:05.850 CST [unknown] 9.0.107.9(48928) postgres tbase 347135 0STATEMENT:  SELECT 100.0 * recv_buffer_used /((CAST(SUBSTRING(current_setting('fn_sh",
                "ErrorTime": "2025-03-20 12:12:05",
                "UserName": "tbase"
            },
            {
                "Database": "postgres",
                "ErrorMessage": "2025-03-20 12:12:05.533 CST [unknown] 9.0.107.24(55078) postgres tbase 347715 0ERROR:  function fn_stat_get_activity(integer, integer) does not exist at character 278 2025-03-20 12:12:05.533 CST [unknown] 9.0.107.24(55078) postgres tbase 347715 0HINT:  No function matches the given name and argument types. You might need to add explicit type casts. 2025-03-20 12:12:05.533 CST [unknown] 9.0.107.24(55078) postgres tbase 347715 0STATEMENT:  SELECT 100.0 * recv_buffer_used /((CAST(SUBSTRING(current_setting('fn",
                "ErrorTime": "2025-03-20 12:12:05",
                "UserName": "tbase"
            }
        ],
        "RequestId": "fb6507d3-0dce-4a63-ad28-d578333e47c6",
        "TotalCount": 2562
    }
}
```

