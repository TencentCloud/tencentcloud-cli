**Example 1: 创建日志集**

创建日志集

Input: 

```
tccli cls CreateLogset --cli-unfold-argument  \
    --LogsetName testname \
    --Tags.0.Key test-tag \
    --Tags.0.Value test-value
```

Output: 
```
{
    "Response": {
        "LogsetId": "dc01b74a-49e4-11eb-b378-0242ac130002",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

