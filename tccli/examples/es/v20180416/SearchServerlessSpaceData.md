**Example 1: 查询space数据**



Input: 

```
tccli es SearchServerlessSpaceData --cli-unfold-argument  \
    --SpaceId space-******** \
    --Uri ***-********/_search \
    --Method GET \
    --Body {"query":{"match_all":{}},"size":2}
```

Output: 
```
{
    "Response": {
        "HttpStatus": 200,
        "Result": "{\"took\":1,\"timed_out\":false,\"_shards\":{\"total\":1,\"successful\":1,\"skipped\":0,\"failed\":0},\"hits\":{\"total\":{\"value\":10000,\"relation\":\"eq\"},\"max_score\":1.0,\"hits\":[{\"_index\":\".ds-zxw-29dviv04-2026.11.25-000001\",\"_type\":\"_doc\",\"_id\":\"bg6XEKIBCDYO2PcuOEj_\",\"_score\":1.0,\"_source\":{\"@timestamp\": \"2026-11-19T02:24:23.581Z\", \"level\": \"INFO\", \"service\": \"pay-service\", \"region\": \"ap-guangzhou\", \"host\": \"node-12\", \"client_ip\": \"10.151.22.52\", \"user_id\": 1642, \"http_method\": \"GET\", \"url_path\": \"/api/v1/orders\", \"status_code\": 200, \"latency_ms\": 89.43, \"message\": \"GET /api/v1/orders handled ok\", \"tags\": [\"gray\"]}},{\"_index\":\".ds-zxw-29dviv04-2026.11.25-000001\",\"_type\":\"_doc\",\"_id\":\"bw6XEKIBCDYO2PcuOEj_\",\"_score\":1.0,\"_source\":{\"@timestamp\": \"2026-11-21T11:58:31.581Z\", \"level\": \"WARN\", \"service\": \"pay-service\", \"region\": \"ap-shanghai\", \"host\": \"node-12\", \"client_ip\": \"10.94.133.212\", \"user_id\": 9666, \"http_method\": \"POST\", \"url_path\": \"/api/v1/users\", \"status_code\": 400, \"latency_ms\": 37.18, \"message\": \"slow or rejected request POST /api/v1/users\", \"tags\": [\"batch\", \"core\"]}}]}}",
        "RequestId": "c83af2a0-9bbf-4040-bd1b-0080823101dc"
    }
}
```

