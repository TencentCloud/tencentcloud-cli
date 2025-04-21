**Example 1: 示例1**



Input: 

```
tccli ioa DescribeIpArea --cli-unfold-argument  \
    --NetworkId 3
```

Output: 
```
{
    "Response": {
        "Data": {
            "Name": "cccccc",
            "IPConfig": "192.168.0.3",
            "NetworkId": 3,
            "CreateTime": "2022-11-28 15:41:52.181574 +0000 UTC",
            "EnableFlag": 1,
            "TotalCount": 1,
            "UpdateTime": "2022-11-28 16:38:10.094308 +0000 UTC",
            "LocationCode": "DF976814d3"
        },
        "RequestId": "d3cb47a0-1728-4d3d-9a7f-7da1f8878b7f"
    }
}
```

