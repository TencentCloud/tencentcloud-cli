**Example 1: 请求示例**

查询直播增强用量明细。

Input: 

```
tccli live DescribeLiveEnhanceInfoList --cli-unfold-argument  \
    --StartTime abc \
    --EndTime abc \
    --Granularity 0 \
    --DomainNames abc \
    --Type abc \
    --Resolution abc \
    --Fps abc
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Domain": "abc",
                "Time": "abc",
                "Duration": 0,
                "Fps": "abc",
                "Resolution": "abc",
                "Type": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

