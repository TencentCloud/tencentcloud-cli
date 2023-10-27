**Example 1: 告警中心-隔离操作示例**

告警中心-隔离操作示例

Input: 

```
tccli cfw CreateAlertCenterIsolate --cli-unfold-argument  \
    --HandleAssetList ins-fwynfguf \
    --HandleTime 7 \
    --AlertDirection 0 \
    --IsolateType 1 2 4 \
    --OmMode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9ed67674-49b2-486b-985b-709f92508601",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

