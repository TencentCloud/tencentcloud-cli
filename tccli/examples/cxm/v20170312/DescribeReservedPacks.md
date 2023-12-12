**Example 1: 查询预扣包**

根据reserved-pack-id查询预扣包。

Input: 

```
tccli cxm DescribeReservedPacks --cli-unfold-argument  \
    --Filters.0.Name reserved-pack-id \
    --Filters.0.Values 9e60dee8-fdf8-4afa-b538-d83bdf9c194f
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ReservedPackSet": [
            {
                "ReservedPackId": "9e60dee8-fdf8-4afa-b538-d83bdf9c194f",
                "Zone": "ap-shanghai-4",
                "InstanceType": "SA2.MEDIUM4",
                "InstanceId": "",
                "Pool": "qcloud",
                "DisasterRecoverGroupIds": [],
                "ReservedPackMatchId": "cls-cifbh7vh_eklet-subnet-lo6b5zu9",
                "Status": "active",
                "ReservedPackName": "eksri-hgy2noon",
                "CreatedTime": "2023-04-23T02:55:10Z"
            }
        ],
        "RequestId": "19775875-64d2-436a-b1d9-63b73da67d99"
    }
}
```

