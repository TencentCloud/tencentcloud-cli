**Example 1: 获取云应用项目高级配置数据**

用于获取云应用高级配置参数

Input: 

```
tccli car DescribeApplicationProjectAdvancedConfig --cli-unfold-argument  \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "ApplicationParams": "abc",
        "Resolution": "abc",
        "FPS": 0,
        "MinBitrate": 0,
        "MaxBitrate": 0,
        "PreloadDuration": "10s",
        "ReconnectTimeout": "10s",
        "DisableVideoCodecs": [
            "H265"
        ],
        "RequestId": "abc"
    }
}
```

