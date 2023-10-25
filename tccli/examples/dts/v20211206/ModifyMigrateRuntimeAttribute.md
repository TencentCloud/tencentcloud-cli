**Example 1: 修改Redis目标库写入模式**

修改Redis目标库写入模式，填写对应参数即可，也可同时修改多个参数。

Input: 

```
tccli dts ModifyMigrateRuntimeAttribute --cli-unfold-argument  \
    --JobId dts-2rgv0f09 \
    --OtherOptions.0.Key DstWriteMode \
    --OtherOptions.0.Value clearData
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

