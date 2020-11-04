**Example 1: 查询负载均衡相关的任务状态**



Input: 

```
tccli ecm DescribeLoadBalanceTaskStatus --cli-unfold-argument  \
    --TaskId a4b58173-34c0-4940-9759-28e06257f3dc
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "6cf00076-1f62-4b28-bdeb-8b2d5b363cb7"
    }
}
```

