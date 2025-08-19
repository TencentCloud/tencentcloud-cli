**Example 1: 查询指定策略详情**



Input: 

```
tccli ioa DescribePolicyDetail --cli-unfold-argument  \
    --PolicyId 291463 \
    --OsType 2 \
    --DomainInstanceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "be6db4f6-5ec9-4aef-9d1c-a2c710be0105",
        "Data": {
            "OsType": 2,
            "Description": "",
            "Status": 1,
            "PolicyType": 2,
            "TimeEffectType": 0,
            "TimeStart": 0,
            "TimeEnd": 0,
            "Priority": 50,
            "PolicySubType": 18,
            "IsBase": 0,
            "Name": "peihe"
        }
    }
}
```

