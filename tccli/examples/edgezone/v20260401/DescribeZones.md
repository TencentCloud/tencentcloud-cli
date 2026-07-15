**Example 1: 查询所有地域账号可用区列表**

查询指定账号在所有已配置地域下的可用区列表，返回跨地域聚合结果。

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
                "Zone": "ap-guangzhou-1",
                "ZoneName": "广州一区",
                "ZoneNameEn": "Guangzhou Zone 1",
                "Region": "ap-guangzhou"
            },
            {
                "ZoneId": 160001,
                "Zone": "ap-chengdu-1",
                "ZoneName": "成都一区",
                "ZoneNameEn": "Chengdu Zone 1",
                "Region": "ap-chengdu"
            }
        ],
        "TotalCount": 2,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

**Example 2: 查询无可用区的账号**

查询未在任何地域关联可用区的账号，返回空列表。

Input: 

```
tccli edgezone DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ZoneSet": [],
        "TotalCount": 0,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

