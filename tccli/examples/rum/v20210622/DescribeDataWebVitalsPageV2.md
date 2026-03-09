**Example 1: 成功**



Input: 

```
tccli rum DescribeDataWebVitalsPageV2 --cli-unfold-argument  \
    --ID 120000 \
    --Type ext3 \
    --CostType avg \
    --StartTime 1745911200 \
    --EndTime 1748427659
```

Output: 
```
{
    "Response": {
        "RequestId": "111802f7-0b90-45ed-a85e-fee8779be41f",
        "Result": "{\"request_id\":\"785802f7-0b90-45ed-a85e-fee8779be41f\",\"results\":[{\"offset\":\"\",\"statement_id\":0,\"total\":0},{\"offset\":\"\",\"statement_id\":1,\"total\":0},{\"offset\":\"\",\"statement_id\":2,\"total\":0},{\"offset\":\"\",\"statement_id\":3,\"total\":0}]}"
    }
}
```

