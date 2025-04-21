**Example 1: 示例1**

创建一个身份源进行数据同步

Input: 

```
tccli ioa CreateIdentifySource --cli-unfold-argument  \
    --Name  \
    --Type WeCom \
    --ExtraConfig {} \
    --SyncEnable True \
    --SyncPolicyParams {"week":"","hour":"","minute":"2"} \
    --Config {"root_id": "1", "attribute_map": {"user_id": "userid", "extended_id": "open_userid", "name": "name", "phone": "mobile", "email": "email", "avatar": "avatar"}, "status_attribute": {"type": "none"}, "corp_id": "wwa83db5512410cb7f", "corp_secret": "eLcniq-D6L7AWMwf4TAPiM9XVlN3S2eMMg50l6xu7h0", "extended_attributes": []} \
    --SyncPolicy 4hours
```

Output: 
```
{
    "Response": {
        "RequestId": "d332f4fb-5989-443b-970d-1d752d08c6e8",
        "Data": {
            "TypeForIoa": 10002,
            "Config": "{\"root_id\": \"1\", \"attribute_map\": {\"user_id\": \"userid\", \"extended_id\": \"open_userid\", \"name\": \"name\", \"phone\": \"mobile\", \"email\": \"email\", \"avatar\": \"avatar\"}, \"status_attribute\": {\"type\": \"none\"}, \"corp_id\": \"wwa83db5512410cb7f\", \"corp_secret\": \"eLcniq-D6L7AWMwf4TAPiM9XVlN3S2eMMg50l6xu7h0\", \"extended_attributes\": []}",
            "SyncEnable": true,
            "Id": "EhK6SmwgxAKDfdKbaWzZcX",
            "CreateTime": "2022-10-21T15:19:14+08:00",
            "PresentInfo": [],
            "Name": "EhK6SmwgxAKDfdKbaWzZcX",
            "SyncPolicy": "4hours",
            "SyncPolicyParams": "{\"week\":\"\",\"hour\":\"\",\"minute\":\"2\"}",
            "Type": "WeCom",
            "UpdateTime": "2022-10-21T15:19:14+08:00",
            "ExtraConfig": "None"
        }
    }
}
```

