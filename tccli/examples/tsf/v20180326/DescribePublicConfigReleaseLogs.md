**Example 1: 查询公共配置发布历史**



Input: 

```
tccli tsf DescribePublicConfigReleaseLogs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "5748271c-3579-4f40-95b9-5f7b87f27388",
        "Result": {
            "TotalCount": 0,
            "Content": []
        }
    }
}
```

