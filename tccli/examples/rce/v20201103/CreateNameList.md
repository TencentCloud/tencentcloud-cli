**Example 1: CreateNameList**



Input: 

```
tccli rce CreateNameList --cli-unfold-argument  \
    --BusinessSecurityData.ListName "手机黑库" \
    --BusinessSecurityData.SceneCode "all_scene" \
    --BusinessSecurityData.Remark "测试" \
    --BusinessSecurityData.DataType 2 \
    --BusinessSecurityData.ListType 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": []
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

