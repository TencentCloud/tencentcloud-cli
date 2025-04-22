**Example 1: 更新索引元数据**

更新索引元数据---- 添加ResourceInUse.IsolatedStatus错误码

Input: 

```
tccli es UpdateServerlessInstance --cli-unfold-argument  \
    --UpdateMetaJson {"mappings":{"properties":{}},"options":{"expire.max_age":"7d"},"settings":{}} \
    --InstanceId index-asdasd
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

