**Example 1: 请求示例**

查询线性组装Source告警信息。

Input: 

```
tccli mps DescribeStreamPackageSourceAlerts --cli-unfold-argument  \
    --SourceId 66503E8E0000930000F1 \
    --StartTime 1590508800 \
    --EndTime 1590508900
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "SourceId": "66503E8E0000930000F1",
                "SourceName": "source_name",
                "Code": 20012,
                "Category": "PLAYBACK_WARNING",
                "Message": "https://test.com/demo.m3u8 request response http 404.",
                "LastModifiedTime": 1590508900
            }
        ],
        "RequestId": "req-xxx"
    }
}
```

