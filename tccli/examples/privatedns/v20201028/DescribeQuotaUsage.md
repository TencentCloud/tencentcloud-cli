**Example 1: 查询用户额度使用情况**



Input: 

```
tccli privatedns DescribeQuotaUsage --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "89aa867e-74db-4fce-9cab-add371622723",
        "TldQuota": {
            "Total": 1,
            "Used": 1,
            "Stock": 5000,
            "Quota": 100
        }
    }
}
```

