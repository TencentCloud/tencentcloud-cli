**Example 1: 配额**



Input: 

```
tccli igtm DescribeQuotas --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Quotas": {
            "TaskQuota": 1,
            "PoolQuota": 1,
            "AddressQuota": 1,
            "MonitorQuota": 1,
            "MessageQuota": 1
        },
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

