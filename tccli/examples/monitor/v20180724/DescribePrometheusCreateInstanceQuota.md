**Example 1: 查询prometheus实例创建配额**



Input: 

```
tccli monitor DescribePrometheusCreateInstanceQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaDetail": {
            "Available": 16,
            "Limit": 20,
            "Usage": 4
        },
        "RequestId": "acfd4482-fec0-43bf-816e-231ba8d41d76"
    }
}
```

