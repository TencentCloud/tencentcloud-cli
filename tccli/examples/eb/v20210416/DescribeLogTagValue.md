**Example 1: 事件查询维度值结果**

事件查询维度值结果

Input: 

```
tccli eb DescribeLogTagValue --cli-unfold-argument  \
    --StartTime 1673233483024 \
    --EndTime 1673838283024 \
    --EventBusId eb-xxxxx \
    --GroupField Source \
    --Page 1 \
    --Limit 1000
```

Output: 
```
{
    "Response": {
        "Results": [
            "cvm.cloud.tencent"
        ],
        "RequestId": "cfa5ba79-4169-44d5-a1c4-a95b8a8b4481"
    }
}
```

