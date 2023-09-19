**Example 1: 编辑订单**

修改订单容量&别名&项目ID

Input: 

```
tccli cwp ModifyLicenseOrder --cli-unfold-argument  \
    --Alias 别名 \
    --ProjectId 0 \
    --ResourceId cwplic-xxxxxxxx \
    --InquireNum 10
```

Output: 
```
{
    "Response": {
        "RequestId": "bfcd9422-e824-4651-8fe3-1af96781ce6e",
        "DealNames": [],
        "ResourceIds": [
            "cwplic-xxxxxxxx"
        ]
    }
}
```

