**Example 1: 查询腾讯云健康看板的实时可用性事件信息**

查询腾讯云健康看板的实时可用性事件信息

Input: 

```
tccli tchd DescribeEventStatistics --cli-unfold-argument  \
    --RegionId ap-nanjing \
    --ProductIds cvm
```

Output: 
```
{
    "Response": {
        "Data": {
            "AbnormalCount": 0,
            "NormalCount": 1,
            "NotifyCount": 0
        },
        "RequestId": "c6847868-264b-4879-b406-9283e708412b"
    }
}
```

