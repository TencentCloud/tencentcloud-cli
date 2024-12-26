**Example 1: 获取云应用项目高级配置数据**

用于获取云应用高级配置参数

Input: 

```
tccli car DescribeApplicationProjectAdvancedConfig --cli-unfold-argument  \
    --ProjectId cap-op8pfan8
```

Output: 
```
{
    "Response": {
        "ApplicationParams": "param 1980",
        "Resolution": "1920*1680",
        "FPS": 0,
        "MinBitrate": 3,
        "MaxBitrate": 6,
        "PreloadDuration": "10s",
        "ReconnectTimeout": "10s",
        "DisableVideoCodecs": [
            "H265"
        ],
        "RequestId": "42439412-a321-439e-83e8-907799b16417"
    }
}
```

