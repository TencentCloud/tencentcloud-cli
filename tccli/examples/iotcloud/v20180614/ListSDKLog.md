**Example 1: 查询设备SDK日志**

查询设备SDK日志

Input: 

```
tccli iotcloud ListSDKLog --cli-unfold-argument  \
    --Keywords productid:xxxxxxx \
    --MinTime 1606205400000 \
    --MaxTime 1606209059999
```

Output: 
```
{
    "Response": {
        "Context": "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAD1JVkWTEk5MHpyTVRTQ3lqa0tVbUtNVm9sZw==",
        "Listover": true,
        "RequestId": "1641d33e-df97-43d4-8cf1-21ba85533336",
        "Results": []
    }
}
```

