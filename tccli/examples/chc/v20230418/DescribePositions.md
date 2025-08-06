**Example 1: 获取机位列表**



Input: 

```
tccli chc DescribePositions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PositionSet": [
            {
                "Height": 2,
                "IdcId": 159,
                "IdcName": "天津数据备份中心东区DC",
                "IdcUnitId": 596,
                "IdcUnitName": "天津数据备份中心东区DC1栋M303",
                "PlanDeviceType": 8,
                "PositionCode": "10",
                "PositionId": 158660,
                "PositionStatus": 0,
                "RackId": 15451,
                "RackName": "M303-C14"
            }
        ],
        "RequestId": "718aa630-5ccb-4ffa-983b-f627c433379e",
        "Total": 37205
    }
}
```

