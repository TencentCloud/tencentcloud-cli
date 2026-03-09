**Example 1: DescribeCreateMySQLResult**



Input: 

```
tccli tcb DescribeCreateMySQLResult --cli-unfold-argument  \
    --EnvId **s*e*-********2dbc0df14561 \
    --TaskId 38654
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailReason": null,
            "FreezeStatus": false,
            "Status": "success"
        },
        "RequestId": "c110db5b-5fd8-4a02-9a86-c2a46679abd7"
    }
}
```

