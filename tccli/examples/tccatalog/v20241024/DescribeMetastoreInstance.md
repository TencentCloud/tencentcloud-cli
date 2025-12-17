**Example 1: 展示metastoreinstance信息**



Input: 

```
tccli tccatalog DescribeMetastoreInstance --cli-unfold-argument  \
    --InstanceId tcc-cqtesta
```

Output: 
```
{
    "Response": {
        "InstanceId": "tcc-cqtesta",
        "RequestId": "68b3ebaf-b91c-4a31-9b1b-6b4c47536513",
        "Status": "Running"
    }
}
```

