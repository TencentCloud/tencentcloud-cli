**Example 1: Copying person**



Input: 

```
tccli iai CopyPerson --cli-unfold-argument  \
    --PersonId 2001 \
    --GroupIds TencentShenZhenEmployee ShenZhenCitizen
```

Output: 
```
{
    "Response": {
        "SucGroupNum": 2,
        "SucGroupIds": [
            "ShenZhenCitizen",
            "TencentShenZhenEmployee"
        ],
        "RequestId": "9841c008-e597-4356-a8d5-c47a246abd8d"
    }
}
```

**Example 2: Sample error**



Input: 

```
tccli iai CopyPerson --cli-unfold-argument  \
    --PersonId 1001 \
    --GroupIds TencentShenZhenEmployee ZhuYuanDormitoryNo1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.GroupPersonMapExist",
            "Message": "The ID of the corresponding person is already in the group."
        },
        "RequestId": "8ecfa566-68a9-4eb5-a6da-95ba9be26947"
    }
}
```

