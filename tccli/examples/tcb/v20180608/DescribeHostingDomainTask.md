**Example 1: 查询环境静态托管域名任务状态**



Input: 

```
tccli tcb DescribeHostingDomainTask --cli-unfold-argument  \
    --EnvId env-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Status": "doing"
    }
}
```

