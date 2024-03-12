**Example 1: 获取备选校验方式**

获取备选校验方式

Input: 

```
tccli account GetBackUpValidate --cli-unfold-argument  \
    --OwnerUin 100000012 \
    --Interface getInfo \
    --ClientUA chrome \
    --Skey LpZhb4CdVm5 \
    --ClientIP 0.0.0.0
```

Output: 
```
{
    "Response": {
        "FaceId": {
            "CanAuth": 1,
            "Data": null
        },
        "Phone": {
            "CanAuth": 1,
            "Data": null
        },
        "Wechat": {
            "CanAuth": 1,
            "Data": null
        },
        "Token": {
            "CanAuth": 1,
            "Data": null
        },
        "Stoken": {
            "CanAuth": 1,
            "Data": null
        },
        "SoftToken": {
            "CanAuth": 1,
            "Data": null
        },
        "U2FToken": {
            "CanAuth": 1,
            "Data": {}
        },
        "Mail": {
            "CanAuth": 1
        },
        "RequestId": "69633ebf-4770-4024-a5f9-3b85d17e1cd0"
    }
}
```

