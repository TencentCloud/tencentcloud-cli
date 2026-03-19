**Example 1: 示例**



Input: 

```
tccli cwp DescribeShellPolicyList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PolicyId": 2001,
                "PolicyName": "系统自动拦截规则(标准)",
                "PolicyType": 0,
                "PolicyDesc": "系统自动拦截规则(标准)",
                "PolicyAction": 2,
                "IsEnabled": 1,
                "UpdateTime": "0000-00-00 00:00:00",
                "HostScope": 2
            },
            {
                "PolicyId": 2002,
                "PolicyName": "系统自动拦截规则(重保)",
                "PolicyType": 0,
                "PolicyDesc": "系统自动拦截规则(重保)",
                "PolicyAction": 2,
                "IsEnabled": 1,
                "UpdateTime": "0000-00-00 00:00:00",
                "HostScope": 2
            }
        ],
        "RequestId": "1d916aa9-5c60-4849-b5d4-be232998382b",
        "TotalCount": 0
    }
}
```

