**Example 1: 预览 Stable 目标**

不创建 Version、不修改 Label；仅返回一次拉取结果。

Input: 

```
tccli ags PreviewRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --Label stable
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "PreviewResult": "{\"StatusCode\": 200, \"Body\": \"{\\\"name\\\":\\\"example.com/weather\\\"}\", \"HasUpdate\": false}",
        "ResolvedVersionId": "rv-0123abcd"
    }
}
```

