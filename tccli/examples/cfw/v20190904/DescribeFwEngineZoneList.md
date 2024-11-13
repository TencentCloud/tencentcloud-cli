**Example 1: 实例1 查询引擎可用区信息**

查询引擎可用区信息

Input: 

```
tccli cfw DescribeFwEngineZoneList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "FwEnginType": "VPC防火墙实例",
                "InstanceId": "cfwew-03198ed3",
                "InstanceName": "测试多点-实例1",
                "IsSingleZone": true,
                "RegionList": [
                    "ap-beijing"
                ],
                "ZoneList": [
                    "ap-beijing-3"
                ],
                "ZoneNameList": [
                    "北京三区"
                ]
            }
        ],
        "RequestId": "7846e970-cd7b-4ab3-ab70-ce6ac1ded6fa"
    }
}
```

