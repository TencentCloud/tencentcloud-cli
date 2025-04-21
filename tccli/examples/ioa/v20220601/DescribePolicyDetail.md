**Example 1: 查询指定策略详情**



Input: 

```
tccli ioa DescribePolicyDetail --cli-unfold-argument  \
    --PolicyId 474
```

Output: 
```
{
    "Response": {
        "RequestId": "be6db4f6-5ec9-4aef-9d1c-a2c710be0105",
        "Data": {
            "Name": "abc",
            "OsType": 0,
            "Priority": 50,
            "PolicyType": 3,
            "Description": "\"\"",
            "Status": 1,
            "TimeEffectType": 0,
            "TimeStart": 0,
            "TimeEnd": 0,
            "PolicySubType": 20,
            "IsBase": 0
        }
    }
}
```

