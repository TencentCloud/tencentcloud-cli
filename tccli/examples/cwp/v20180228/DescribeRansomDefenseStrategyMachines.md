**Example 1: 查询防勒索策略绑定机器列表**

查询防勒索策略绑定机器列表

Input: 

```
tccli cwp DescribeRansomDefenseStrategyMachines --cli-unfold-argument  \
    --Id 1 \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "MachineName": "销售许可测试机器",
                "InstanceId": "ins-ddad",
                "MachineIp": "10.0.0.2",
                "MachineWanIp": "xx.xx.xx.xx",
                "CloudTags": [],
                "RegionInfo": {
                    "Region": "ap-guangzhou",
                    "RegionCode": "gz",
                    "RegionId": 1,
                    "RegionName": "华南地区（广州）",
                    "RegionNameEn": "South China (Guangzhou)"
                },
                "Tag": [
                    {
                        "Rid": 16069,
                        "Name": "apitest",
                        "TagId": 16069
                    }
                ],
                "Status": 1,
                "StrategyId": 5570,
                "StrategyName": "tt1",
                "DiskInfo": "diskId1|diskName1;diskId2|diskName2",
                "HostVersion": 2
            }
        ],
        "RequestId": "544961cc-1ee0-4a5f-9752-7489afa407ef"
    }
}
```

