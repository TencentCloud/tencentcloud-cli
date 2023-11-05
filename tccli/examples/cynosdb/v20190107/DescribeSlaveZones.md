**Example 1: DescribeSlaveZones**



Input: 

```
tccli cynosdb DescribeSlaveZones --cli-unfold-argument  \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "SlaveZones": [
            "ap-guangzhou-5"
        ],
        "RequestId": "128046"
    }
}
```

