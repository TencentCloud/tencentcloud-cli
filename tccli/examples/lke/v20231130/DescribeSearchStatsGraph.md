**Example 1: 查询搜索服务调用折线图示例**

查询搜索服务调用折线图示例

Input: 

```
tccli lke DescribeSearchStatsGraph --cli-unfold-argument  \
    --ModelName cs-normal-70b \
    --StartTime 1758988800 \
    --EndTime 1759075199 \
    --SpaceId default_space \
    --StatStartTime 1758988800 \
    --StatEndTime 1759075199
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "cef68b22-98ba-435a-be50-c57d936949f2"
    }
}
```

