**Example 1: 删除Redis实例的大key分析任务**

删除Redis实例的大key分析任务。

Input: 

```
tccli dbbrain DeleteRedisBigKeyAnalysisTasks --cli-unfold-argument  \
    --Product redis \
    --InstanceId crs-0hnhwega \
    --AsyncRequestIds 11822173
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "e9833850-b223-18ee-8376-93f024a9a071"
    }
}
```

