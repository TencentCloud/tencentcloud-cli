**Example 1: 查询各种clb运行状态数目**

查询各种clb运行状态数目

Input: 

```
tccli clb DescribeLoadBalancerOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RunningCount": 0,
        "IsolationCount": 0,
        "WillExpireCount": 0,
        "RequestId": "03b18184-caf1-40d7-b01a-8a76565b94ad"
    }
}
```

