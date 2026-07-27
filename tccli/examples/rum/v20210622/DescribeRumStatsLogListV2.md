**Example 1: success**



Input: 

```
tccli rum DescribeRumStatsLogListV2 --cli-unfold-argument  \
    --StartTime 1665993060000 \
    --Limit 100 \
    --Filter [{"Key": "instanceId", "Operator": "eq", "Value": "rum-xyz"}] \
    --EndTime 1665996660000 \
    --ID 100
```

Output: 
```
{
    "Response": {
        "RequestId": "a6bafa2f-3f6a-4f1a-b9a3-d1d848d34168",
        "Result": "[{\"timestamp\":1784564220,\"count\":3},{\"timestamp\":1784564280,\"count\":2},{\"timestamp\":1784564340,\"count\":20},{\"timestamp\":1784564400,\"count\":22}]"
    }
}
```

