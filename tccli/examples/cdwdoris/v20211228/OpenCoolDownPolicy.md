**Example 1: 开通**



Input: 

```
tccli cdwdoris OpenCoolDownPolicy --cli-unfold-argument  \
    --InstanceId doris-12345678 \
    --DatabaseName sales_db \
    --TableName customer_orders \
    --OperationType enable
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "Operation successful",
        "QueryDocument": "[{\"partition_name\": \"p1\", \"cool_down_status\": \"enabled\", \"cool_down_policy\": \"policy_7days\"}, {\"partition_name\": \"p2\", \"cool_down_status\": \"disabled\", \"cool_down_policy\": \"\"}]",
        "RequestId": "req-987654321"
    }
}
```

