**Example 1: 获取ES字段聚合结果**



Input: 

```
tccli tcss DescribeESAggregations --cli-unfold-argument  \
    --Query {"index":[],"body":"{\"query\":{\"bool\":{\"filter\":{\"bool\":{\"filter\":{\"range\":{\"insert_time\":{\"gt\":1729737627694,\"lte\":1729766427694}}},\"must\":[],\"must_not\":[],\"should\":[]}}}},\"highlight\":{\"fields\":{\"*\":{}}},\"aggs\":{\"count_stats\":{\"date_histogram\":{\"field\":\"insert_time\",\"interval\":\"30m\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"track_total_hits\":true,\"sort\":[{\"insert_time\":\"desc\"}]}"} \
    --LogTypes asset_container asset_local_image asset_registry_image asset_host asset_cluster asset_pod asset_service asset_ingress asset_process asset_port asset_web_service asset_app asset_db container_bash container_launch k8s_api local_image_virus local_image_risk local_image_vul registry_image_virus registry_image_risk registry_image_vul image_deny cluster_risk_vul cluster_risk_cfg baseline_docker_container baseline_docker_image baseline_docker_host baseline_containerd_container baseline_k8s baseline_containerd_host container_escape reverse_shell container_virus malicious_connection abnormal_process access_control risk_syscall abnormal_k8s_api
```

Output: 
```
{
    "Response": {
        "Data": "{\"took\":973,\"hits\":{\"total\":{\"value\":5108036,\"relation\":\"eq\"}},\"aggregations\":{\"count_stats\":{\"buckets\":[{\"key_as_string\":\"2024-10-24T10:30:00.000+08:00\",\"key\":1729737000000,\"doc_count\":47623},{\"key_as_string\":\"2024-10-24T11:00:00.000+08:00\",\"key\":1729738800000,\"doc_count\":64848},{\"key_as_string\":\"2024-10-24T11:30:00.000+08:00\",\"key\":1729740600000,\"doc_count\":65760},{\"key_as_string\":\"2024-10-24T12:00:00.000+08:00\",\"key\":1729742400000,\"doc_count\":71743},{\"key_as_string\":\"2024-10-24T12:30:00.000+08:00\",\"key\":1729744200000,\"doc_count\":72563},{\"key_as_string\":\"2024-10-24T13:00:00.000+08:00\",\"key\":1729746000000,\"doc_count\":65545},{\"key_as_string\":\"2024-10-24T13:30:00.000+08:00\",\"key\":1729747800000,\"doc_count\":63693},{\"key_as_string\":\"2024-10-24T14:00:00.000+08:00\",\"key\":1729749600000,\"doc_count\":71868},{\"key_as_string\":\"2024-10-24T14:30:00.000+08:00\",\"key\":1729751400000,\"doc_count\":73547},{\"key_as_string\":\"2024-10-24T15:00:00.000+08:00\",\"key\":1729753200000,\"doc_count\":65341},{\"key_as_string\":\"2024-10-24T15:30:00.000+08:00\",\"key\":1729755000000,\"doc_count\":64074},{\"key_as_string\":\"2024-10-24T16:00:00.000+08:00\",\"key\":1729756800000,\"doc_count\":877499},{\"key_as_string\":\"2024-10-24T16:30:00.000+08:00\",\"key\":1729758600000,\"doc_count\":914717},{\"key_as_string\":\"2024-10-24T17:00:00.000+08:00\",\"key\":1729760400000,\"doc_count\":823727},{\"key_as_string\":\"2024-10-24T17:30:00.000+08:00\",\"key\":1729762200000,\"doc_count\":743536},{\"key_as_string\":\"2024-10-24T18:00:00.000+08:00\",\"key\":1729764000000,\"doc_count\":756934},{\"key_as_string\":\"2024-10-24T18:30:00.000+08:00\",\"key\":1729765800000,\"doc_count\":265018}]}},\"_shards\":{\"total\":9,\"successful\":9,\"failed\":0}}",
        "RequestId": "16fd0b2f-6bae-426e-bf63-64607a7e2705"
    }
}
```

