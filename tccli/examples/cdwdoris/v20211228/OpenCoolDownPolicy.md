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
        "QueryDocument": "SELECT * FROM customer_orders LIMIT 10",
        "RequestId": "req-987654321"
    }
}
```

