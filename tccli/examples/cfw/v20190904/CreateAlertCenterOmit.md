**Example 1: 告警中心-忽略操作示例**

告警中心-忽略操作示例

Input: 

```
tccli cfw CreateAlertCenterOmit --cli-unfold-argument  \
    --HandleIdList ad397c0849e28d39d29a711011f725a9 \
    --TableType AlertTable
```

Output: 
```
{
    "Response": {
        "RequestId": "ed72cd04-be0e-4925-9fcc-1d857ed1312c",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

