**Example 1: 查询所有地域账号边缘可用区列表**



Input: 

```
tccli edgezone DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ZoneSet": [
            {
                "ZoneId": 100001,
                "Zone": "ap-guangzhou-tez-gz-1",
                "ZoneName": "广州边缘一区",
                "ZoneNameEn": "Guangzhou Edge Zone 1",
                "Region": "ap-guangzhou"
            },
            {
                "ZoneId": 160001,
                "Zone": "ap-chengdu-tez-cd-1",
                "ZoneName": "成都边缘一区",
                "ZoneNameEn": "Chengdu Edge Zone 1",
                "Region": "ap-chengdu"
            }
        ],
        "TotalCount": 2,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

