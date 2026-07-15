**Example 1: 查询日志**

查询protocol为HTTP的日志

Input: 

```
tccli cfw SearchLog --cli-unfold-argument  \
    --TopicId cfw_netflow_border \
    --From 1782131614167 \
    --To 1782736414167 \
    --Query protocol:HTTP \
    --SamplingRate 1 \
    --SyntaxRule 1 \
    --Limit 1 \
    --Context  \
    --Sort desc \
    --UseNewAnalysis True
```

Output: 
```
{
    "Response": {
        "Analysis": false,
        "Context": "Y29udGV4dC0wMmUyNmVmYi05OTZiLTQzNTctYTA1Ny03OGY1NmU3ZmRmNzUxNzgyNzM2NDc1NzE5",
        "ListOver": false,
        "RequestId": "e660b374-1538-4631-be77-c9a6e6680180",
        "Results": [
            {
                "FileName": "",
                "LogJson": "{\"instance_id\":\"ins-gke2r5e0\",\"src_ip\":\"119.**.**.112\",\"dst_ip\":\"103.**.**.115\",\"src_port\":56980,\"dst_port\":80,\"protocol\":\"HTTP\",\"direction\":0,\"dst_domain\":\"www.**.com\",\"in_pkt_count\":8,\"in_pkt_len\":2998,\"out_pkt_count\":8,\"out_pkt_len\":416,\"total_pkt_count\":16,\"total_pkt_len\":3414,\"ti_tag\":\"\",\"start_time\":\"2026-06-29 14:12:11\",\"end_time\":\"2026-06-29 14:12:24\",\"supplier\":\"baidu.com\",\"src_country\":\"\",\"dst_country\":\"中国\",\"src_province\":\"\",\"dst_province\":\"广东省\",\"src_city\":\"\",\"dst_city\":\"\",\"address\":\"广东省\",\"src_lat\":0,\"dst_lat\":0,\"src_lon\":0,\"dst_lon\":0,\"insert_time\":1782713553,\"count\":0,\"url\":\"\",\"domain_flag\":0,\"port_status\":0,\"level\":0,\"bot_flag\":0,\"mode\":1,\"tcp_flag\":31,\"timestamp\":\"2026-06-29 14:12:11\",\"is_serial\":1,\"pkt_flags\":\"0212101810\",\"pkt_dir\":\"01001\",\"action_src\":1,\"acl_uuid\":\"\",\"acl_rule_id\":0,\"acl_detail\":\"\"}",
                "PkgId": "5229A51C7BECDA416A3E478F-00000000000579C7",
                "PkgLogId": "29622640",
                "RawLog": "",
                "Time": 1782713531000,
                "TopicId": "cfw_netflow_border"
            }
        ],
        "SamplingRate": 0
    }
}
```

