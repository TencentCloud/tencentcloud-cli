**Example 1: 查询应用更新触发器触发日志**



Input: 

```
tccli tcr DescribeApplicationTriggerLogPersonal --cli-unfold-argument  \
    --RepoName test/test123
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1
        },
        "RequestId": "7d27c2f4-0473-484c-b62e-fcb379758289"
    }
}
```

