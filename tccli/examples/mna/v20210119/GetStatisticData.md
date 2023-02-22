**Example 1: 获取指定id的设备流量用量统计文件**

获取流量统计数据

Input: 

```
tccli mna GetStatisticData --cli-unfold-argument  \
    --EndTime 1659514692 \
    --DeviceId xx \
    --TimeGranularity 1 \
    --BeginTime 1659513692
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "FilePath": "http://geekyang-cos-1257943044.cos-internal.ap-guangzhou.tencentcos.cn/test/175527768616861696.xlsx"
    }
}
```

