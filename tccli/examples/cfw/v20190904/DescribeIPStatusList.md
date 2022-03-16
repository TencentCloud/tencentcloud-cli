**Example 1: 告警中心-资产安全事件统计-资产详情**



Input: 

```
tccli cfw DescribeIPStatusList --cli-unfold-argument  \
    --IPList 1.2.3.4
```

Output: 
```
{
    "Response": {
        "StatusList": [
            {
                "Status": 0,
                "IP": "xx"
            }
        ],
        "ReturnCode": 0,
        "ReturnMsg": "Success",
        "RequestId": "xx"
    }
}
```

