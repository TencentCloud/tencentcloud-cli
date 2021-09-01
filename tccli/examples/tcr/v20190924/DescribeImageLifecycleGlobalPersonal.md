**Example 1: 获取个人版全局自动清理策略**



Input: 

```
tccli tcr DescribeImageLifecycleGlobalPersonal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "StrategyInfo": [
                {
                    "Username": "3321337994",
                    "RepoName": "",
                    "Type": "global_keep_last_nums",
                    "Value": 80,
                    "Valid": 1,
                    "CreationTime": "2020-01-22 15:38:19 +0800 CST"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

