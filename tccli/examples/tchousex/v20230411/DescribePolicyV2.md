**Example 1: 策略列表V2**



Input: 

```
tccli tchousex DescribePolicyV2 --cli-unfold-argument  \
    --InstanceId instance-o2xk5lup \
    --Limit 200 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "ReturnData": "{\"total\":7,\"list\":[{\"policyId\":496,\"policyName\":\"hangguolv创建失败\",\"policyType\":2,\"policyState\":2,\"updateTime\":\"2025-08-15 14:39:35\",\"database\":\"data_mask1\",\"table\":\"orders_1\",\"column\":\"\",\"ErrMessage\":\"\",\"Rules\":[{\"Condition\":\"amount \\u003e 10\",\"ErrMessage\":\"\",\"Users\":[\"u2\"],\"Roles\":[\"\"]}]},{\"policyId\":497,\"policyName\":\"hanguolv创建成功\",\"policyType\":2,\"policyState\":2,\"updateTime\":\"2025-08-15 14:38:57\",\"database\":\"data_mask1\",\"table\":\"orders_2\",\"column\":\"\",\"ErrMessage\":\"行过滤规则校验失败\",\"Rules\":[{\"Condition\":\"amount \\u003e 10\",\"ErrMessage\":\"\",\"Users\":[\"u2\"],\"Roles\":[\"r3\"]}]},{\"policyId\":115,\"policyName\":\"hanggulv1\",\"policyType\":2,\"policyState\":11,\"updateTime\":\"2025-08-15 11:04:47\",\"database\":\"inside_db\",\"table\":\"tbl_col13_parquet\",\"column\":\"\",\"ErrMessage\":\"行过滤规则校验失败\",\"Rules\":[{\"Condition\":\"f1_int \\u003e 10\",\"ErrMessage\":\"\",\"Users\":[\"cam:100012695507\"],\"Roles\":[\"\"]},{\"Condition\":\"f1_int \\u003e 100\",\"ErrMessage\":\"\",\"Users\":[\"cam:100006811818\"],\"Roles\":[\"\"]}]},{\"policyId\":421,\"policyName\":\"列脱敏删除用户测试\",\"policyType\":1,\"policyState\":2,\"updateTime\":\"2025-08-14 16:01:38\",\"database\":\"data_mask1\",\"table\":\"orders\",\"column\":\"user_id\",\"ErrMessage\":\"\",\"Rules\":[{\"Condition\":\"HASH\",\"ErrMessage\":\"\",\"Users\":[\"u2\"],\"Roles\":[\"\"]}]},{\"policyId\":156,\"policyName\":\"status关键字\",\"policyType\":1,\"policyState\":2,\"updateTime\":\"2025-08-06 17:42:09\",\"database\":\"inside_db\",\"table\":\"orders_1\",\"column\":\"status\",\"ErrMessage\":\"\",\"Rules\":[{\"Condition\":\"HASH\",\"ErrMessage\":\"\",\"Users\":[\"\"],\"Roles\":[\"\"]}]},{\"policyId\":117,\"policyName\":\"列脱敏222\",\"policyType\":1,\"policyState\":2,\"updateTime\":\"2025-08-04 14:59:57\",\"database\":\"inside_db1\",\"table\":\"tbl_col13_parquet\",\"column\":\"f3_varchar\",\"ErrMessage\":\"\",\"Rules\":[]},{\"policyId\":116,\"policyName\":\"lietuomin\",\"policyType\":1,\"policyState\":2,\"updateTime\":\"2025-08-04 14:57:39\",\"database\":\"inside_db\",\"table\":\"tbl_col13_parquet\",\"column\":\"f3_varchar\",\"ErrMessage\":\"\",\"Rules\":[{\"Condition\":\"HASH\",\"ErrMessage\":\"\",\"Users\":[\"cam:100012695507\"],\"Roles\":[\"\"]},{\"Condition\":\"Redact\",\"ErrMessage\":\"\",\"Users\":[\"cam:100006811818\"],\"Roles\":[\"\"]}]}]}",
        "RequestId": "f8c2e52d-b05f-4f48-9f33-51a0a41a5ef5"
    }
}
```

