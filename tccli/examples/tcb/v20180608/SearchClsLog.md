**Example 1: 搜索云函数日志**

搜索云函数日志

Input: 

```
tccli tcb SearchClsLog --cli-unfold-argument  \
    --Context  \
    --EndTime 2026-01-28 23:52:17 \
    --EnvId tcb-xxxx21d05d \
    --Limit 1 \
    --QueryString (src:app OR src:system) AND log:"START RequestId*" \
    --StartTime 2026-01-28 06:47:17 \
    --Sort desc \
    --UseLucene True
```

Output: 
```
{
    "Response": {
        "LogResults": {
            "AnalysisRecords": [],
            "Context": "Y29udGV4dC04ZjdiNGM5Ni01YzY0LTRjxxxxxxxxJjNTBkNTI0ZWIxNzY5NzU2NjgyNDA0",
            "ListOver": false,
            "Results": [
                {
                    "Content": "{\"memory\":\"512\",\"status_code\":\"202\",\"log\":\"START RequestId: 895f3b00-a4b2-4bab-\",\"stamp\":\"MINI_QCBASE\",\"ret_msg\":\"\",\"tcb_log\":\"\",\"function_invoke_time\":\"1769615520200\",\"duration\":\"0\",\"event_type\":\"1\",\"alias\":\"\",\"function_id\":\"lam-5c5gwci3\",\"log_size\":\"53\",\"wan_traffic\":\"0\",\"cluster_name\":\"ap-shanghai-tcb-cube-1\",\"caller_ip\":\"\",\"report_ip\":\"\",\"src\":\"system\",\"bill_duration\":\"0\",\"request_source\":\"TRIGGER_TIMER\",\"retry_num\":\"0\",\"start_time\":\"1769615520193\",\"caller\":\"Worker\",\"mem_duration\":\"0\",\"@timestamp\":\"1769615520200960\",\"mem_usage\":\"0\",\"function_invoke_end_time\":\"0\",\"user_id\":\"1252168680\",\"function_name\":\"near-quertz-area\",\"qualifier\":\"$LATEST\",\"namespace\":\"xxxx-4cs57821d05d\",\"status_msg\":\"\",\"request_id\":\"895f3b00xxxx-4bab-a\",\"ret_code\":\"2\",\"container_id\":\"21f173acc8264785xxxxx8e6485645\"}",
                    "FileName": "",
                    "Source": "",
                    "Timestamp": "2026-01-28 23:52:00.200",
                    "TopicId": "a160184c-xxxx",
                    "TopicName": "tcb-topic-xxxx"
                }
            ]
        },
        "RequestId": "4f4396f8-cccd-4c6cxxxx-865f7c45e"
    }
}
```

**Example 2: 搜索模型日志**

搜索模型日志

Input: 

```
tccli tcb SearchClsLog --cli-unfold-argument  \
    --Context  \
    --EndTime 2026-01-30 23:52:17 \
    --EnvId tcb-xxxx21d05d \
    --Limit 1 \
    --QueryString module:model \
    --StartTime 2026-01-29 06:47:17 \
    --Sort desc \
    --UseLucene True
```

Output: 
```
{
    "Response": {
        "LogResults": {
            "AnalysisRecords": [],
            "Context": "",
            "ListOver": true,
            "Results": [
                {
                    "Content": "{\"msg\":\"数据模型业务日志。\\n操作类型：wedaCre。\\n环境类型：正式环境。\\n请求耗时：102。\",\"eventId\":\"<nil>\",\"level\":\"info\",\"indexAdvise\":\"<nil>\",\"module\":\"model\",\"query\":\"{\\\"data\\\":{\\\"statistics_date\\\":1769616000000,\\\"recharge_newuser_amount\\\":0,\\\"recharge_newuser_count\\\":0,\\\"recharge_count\\\":0,\\\"recharge_amount\\\":0,\\\"recharge_user_count\\\":0,\\\"increase_user_count\\\":0}}\",\"errorMessage\":\"<nil>\",\"errorCode\":\"<nil>\",\"resourceName\":\"playlet_index_9odvef9\",\"envId\":\"lowcode-4gs26nnz095fxxx\",\"envType\":\"prod\",\"requestId\":\"99501bc2-fd11f0-bc30-xxxx\",\"action\":\"wedaCreateV2\",\"dataHubName\":\"default\",\"startTime\":\"2026-01-29T16:00:17.690Z\",\"timeCost\":\"102ms\",\"timestamp\":\"1769702417690\"}",
                    "FileName": "",
                    "Source": "",
                    "Timestamp": "2026-01-30 00:00:17.690",
                    "TopicId": "0123a7d7-8386-403cxxxx-0a9966640c22",
                    "TopicName": "tcb-topic-xxxx-4gs26nnz095f6f4d"
                }
            ]
        },
        "RequestId": "2989d059-2271-xxxxd18-58e24897ef1f"
    },
    "reqId": "f17029de-791d-4f9d-xxxx-dc758b16e8e7"
}
```

**Example 3: 聚合分析日志结果**



Input: 

```
tccli tcb SearchClsLog --cli-unfold-argument  \
    --Context  \
    --EnvId aitest-9g96e4tn46773d08 \
    --StartTime 2026-01-29 06:47:17 \
    --EndTime 2026-01-30 23:52:17 \
    --QueryString * | select request_id, max(status_code) as status  where (request_id='35b9abe7-xxxx-11f1-9ce5-52540059feef' AND retry_num=0)) AND status_code!=202 group by request_id, retry_num \
    --Sort desc \
    --UseLucene True \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "LogResults": {
            "AnalysisRecords": [
                "{\"request_id\":\"35b9abe7-xxxx-11f1-9ce5-52540059feef\",\"status\":200}",
                "{\"request_id\":\"640c1490-xxxx-11f1-823c-525400a9be57\",\"status\":200}"
            ],
            "Context": "",
            "ListOver": true,
            "Results": []
        },
        "RequestId": "27108be7-20ac-xxxx927a-4c5aaa2c4969"
    }
}
```

