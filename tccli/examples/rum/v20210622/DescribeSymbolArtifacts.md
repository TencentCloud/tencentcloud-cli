**Example 1: 查询符号制品**



Input: 

```
tccli rum DescribeSymbolArtifacts --cli-unfold-argument  \
    --Kind js_sourcemap \
    --AppId ****** \
    --Release npm-demo-1.0.6-ip202 \
    --Status active \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "Result": "{\"artifacts\":[{\"app_id\":\"******\",\"artifact_id\":\"s***************************a8*********************6\",\"content_type\":\"application/json\",\"created_at\":\"2026-07-06T19:50:55+08:00\",\"file_name\":\"demo.min.js\",\"file_size\":455508,\"file_type\":\"minified\",\"kind\":\"js_sourcemap\",\"minified_url\":\"http://127.0.0.1:4173/demo.min.js\",\"normalized_url\":\"http://127.0.0.1:4173/demo.min.js\",\"release\":\"npm-demo-1.0.6-ip202\",\"sha256\":\"bb407a9734b1f0ea190637a7c8dedef3c86ce10dea87926d7dfb008b59e830c4\",\"status\":\"active\",\"updated_at\":\"2026-07-09T15:21:42+08:00\",\"uploaded_by\":\"600000563044\",\"validation_status\":\"valid\"},{\"app_id\":\"146683\",\"artifact_id\":\"sma_ea0a032e91330af8ce3961dd4b4b095742441f329d051da8\",\"content_type\":\"application/json\",\"created_at\":\"2026-07-06T16:56:57+08:00\",\"file_name\":\"demo.min.js.map\",\"file_size\":1834677,\"file_type\":\"sourcemap\",\"kind\":\"js_sourcemap\",\"minified_url\":\"http://127.0.0.1:4173/demo.min.js\",\"normalized_url\":\"http://127.0.0.1:4173/demo.min.js\",\"release\":\"npm-demo-1.0.6-ip202\",\"sha256\":\"d336575e1877360a7758f0b7d9bd8c5b59b215e80eb037514135a9c5a10b3a84\",\"status\":\"active\",\"updated_at\":\"2026-07-09T15:10:00+08:00\",\"uploaded_by\":\"700001793941\",\"validation_status\":\"valid\"}],\"next_cursor\":\"\",\"total\":2}",
        "RequestId": "0eee0ba3-98f5-4ef5-beb1-73a67ff8ce60"
    }
}
```

