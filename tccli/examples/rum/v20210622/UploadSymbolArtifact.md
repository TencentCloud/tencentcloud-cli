**Example 1: 登记符号制品**



Input: 

```
tccli rum UploadSymbolArtifact --cli-unfold-argument  \
    --Kind js_sourcemap \
    --FileSize 455508 \
    --Sha256 bb407a9734b1f0ea190637a7c8dedef3c86ce10dea87926d7dfb008b59e830c4 \
    --COSUrl https://tdem-1253358381.cos.ap-guangzhou.myqcloud.com/sourcemaps/146683/npm-demo-1.0.6-ip202/_/4330b986dc15a63594826576800499ba/demo.min.js \
    --AppId 146683 \
    --Release npm-demo-1.0.6-ip202 \
    --MinifiedUrl http://127.0.0.1:4173/demo.min.js \
    --FileType minified \
    --FileName demo.min.js \
    --ContentType application/json
```

Output: 
```
{
    "Response": {
        "Result": "{\"app_id\":\"******\",\"artifact_id\":\"***************d3e8aca92***************86c7c12f5d336\",\"content_type\":\"application/json\",\"created_at\":\"2026-07-06T19:50:55+08:00\",\"file_name\":\"********.js\",\"file_size\":455508,\"file_type\":\"minified\",\"idempotent\":true,\"kind\":\"js_sourcemap\",\"minified_url\":\"http://127.0.0.1:4173/demo.min.js\",\"normalized_url\":\"http://127.0.0.1:4173/demo.min.js\",\"release\":\"npm-demo-1.0.6-ip202\",\"sha256\":\"bb407a9734b1f0ea190637a7c8dedef3c86ce10dea87926d7dfb008b59e830c4\",\"status\":\"active\",\"updated_at\":\"2026-07-09T15:21:43.862917077+08:00\",\"uploaded_by\":\"600000563044\",\"validation_status\":\"valid\"}",
        "RequestId": "0b0cac0a-6b41-4bf1-930e-6b82dd8515f5"
    }
}
```

