**Example 1: 示例**

修改配置参数

Input: 

```
tccli cdwch ModifyInstanceKeyValConfigs --cli-unfold-argument  \
    --InstanceId cdwch-aiqnqpx \
    --UpdateItems.0.ConfKey keep_alive_timeout \
    --UpdateItems.0.ConfValue 100 \
    --DeleteItems.ConfKey max_open_files \
    --DeleteItems.ConfValue 1 \
    --AddItems.0.ConfKey uncompressed_cache_size \
    --AddItems.0.ConfValue 8589934592
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "asdpoqe02312312asdfqwasd",
        "FlowId": 0
    }
}
```

