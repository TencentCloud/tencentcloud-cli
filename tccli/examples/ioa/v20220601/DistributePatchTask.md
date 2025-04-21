**Example 1: 下发补丁任务**

下发补丁任务

Input: 

```
tccli ioa DistributePatchTask --cli-unfold-argument  \
    --Owner admin \
    --BusinessId 123 \
    --SubId 123 \
    --OsType 0 \
    --Data "" \
    --Selects.0.ObjType 0 \
    --Selects.0.Objections 2 \
    --VulTaskType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Mid": [
                "A021C770C7686FC5601F00B40D93B75560A20D15"
            ],
            "Seq": 27
        },
        "RequestId": "6a7c4954-08c5-4403-8a6d-bac650447f18"
    }
}
```

**Example 2: DistributePatchTask**

DistributePatchTask

Input: 

```
tccli ioa DistributePatchTask --cli-unfold-argument  \
    --Owner admin \
    --BusinessId 110 \
    --SubId 103 \
    --OsType 0 \
    --Data {} \
    --Selects.0.ObjType 0 \
    --Selects.0.Objections 4261 \
    --VulTaskType 4 \
    --VulPatchList 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "a5e83cc9-94b8-48ca-8ce1-0a8055625682"
    }
}
```

