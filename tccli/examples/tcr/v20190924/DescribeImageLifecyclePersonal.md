**Example 1: 获取个人版仓库自动清理策略**



Input: 

```
tccli tcr DescribeImageLifecyclePersonal --cli-unfold-argument  \
    --RepoName dockerhub/test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "StrategyInfo": [
                {
                    "Username": "3321337994",
                    "RepoName": "dockerhub/test",
                    "Type": "keep_last_days",
                    "Value": 9223372036854776000,
                    "Valid": 1,
                    "CreationTime": "2020-01-22 15:38:19 +0800 CST"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

