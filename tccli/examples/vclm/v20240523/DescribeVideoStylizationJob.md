**Example 1: 成功调用**

成功调用

Input: 

```
tccli vclm DescribeVideoStylizationJob --cli-unfold-argument  \
    --JobId c5daf8f7077d41a69c13aab31a7164f3
```

Output: 
```
{
    "Response": {
        "JobId": "c5daf8f7077d41a69c13aab31a7164f3",
        "RequestId": "75530f83-a534-47c6-9506-21e1f06d6c5c",
        "ResultVideoUrl": "",
        "StatusCode": "JobRunning",
        "StatusMsg": "处理中"
    }
}
```

