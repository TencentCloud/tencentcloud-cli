**Example 1: 删除符号制品**



Input: 

```
tccli rum DeleteSymbolArtifact --cli-unfold-argument  \
    --Kind js_sourcemap \
    --ArtifactId sma_123e1a8f7d5d3e8aca92b35ca8cd1b5eaef86c7c12f5d336 \
    --AppId 146683
```

Output: 
```
{
    "Response": {
        "Result": "{\"artifact_id\":\"****************************************************\",\"deleted_at\":\"2026-07-09T07:31:22.004165362Z\",\"status\":\"deleted\"}",
        "RequestId": "b9c88351-28af-446a-9b15-3a84b09134b8"
    }
}
```

