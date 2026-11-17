**Example 1: 查询实例账号**



Input: 

```
tccli keewidb DescribeInstanceAccount --cli-unfold-argument  \
    --InstanceId kee-p04nodnb \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Accounts": [
            {
                "AccountName": "root",
                "InstanceId": "kee-p04nodnb",
                "Privilege": "rw",
                "ReadonlyPolicy": [
                    "replication"
                ],
                "Remark": "default",
                "Status": 2
            }
        ],
        "TotalCount": 2,
        "RequestId": "5b761f9f-0240-4b44-9cdf-1b03b88da780"
    }
}
```

