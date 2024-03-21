**Example 1: 获取域名webshell 状态**



Input: 

```
tccli waf DescribeWebshellStatus --cli-unfold-argument  \
    --Domain www.qcloudwaf.com
```

Output: 
```
{
    "Domain": "www.qcloudwaf.com",
    "Status": 0,
    "RequestId": "2d510f3e-9ac9-4282-a62d-9efa61c9825d"
}
```

