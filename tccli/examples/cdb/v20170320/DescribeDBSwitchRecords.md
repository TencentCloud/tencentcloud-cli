**Example 1: Querying instance switch records**



Input: 

```
tccli cdb DescribeDBSwitchRecords --cli-unfold-argument  \
    --InstanceId cdb-nrdbtr5o
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "SwitchTime": "2017-11-07 15:15:48",
                "SwitchType": "TRANSFER"
            }
        ]
    }
}
```

