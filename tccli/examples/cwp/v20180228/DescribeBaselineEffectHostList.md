**Example 1: 基线影响主机列表接口**

根据基线id查询基线影响主机列表数据

Input: 

```
tccli cwp DescribeBaselineEffectHostList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --BaselineId 100441 \
    --StrategyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 21,
        "EffectHostList": [
            {
                "PassCount": 100,
                "FailCount": 100,
                "FirstScanTime": "2019-12-25 11:57:15",
                "LastScanTime": "2019-12-25 11:57:15",
                "Status": 0,
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "HostIp": "xx.xx.xx.xx",
                "AliasName": "销售许可测试机器"
            }
        ]
    }
}
```

