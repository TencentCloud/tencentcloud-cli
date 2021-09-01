**Example 1: 查询负载均衡实例异步任务的执行情况**



Input: 

```
tccli bmlb DescribeLoadBalancerTaskResult --cli-unfold-argument  \
    --TaskId 2385688
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "21cc57b1-83df-49a7-839a-2d6a78c28098"
    }
}
```

