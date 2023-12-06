**Example 1: 示例1**



Input: 

```
tccli mna OrderFlowPackage --cli-unfold-argument  \
    --PackageType DEVICE_1_FLOW_20G \
    --DeviceList mna-test1 mna-test2 \
    --AutoRenewFlag True \
    --PackageRegion 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1206563f-f13f-4647-aaa8-37fa86954cc4-1",
        "ResourceId": "56d11777-50f7-4c60-9c89-e7076c8529a9-0"
    }
}
```

