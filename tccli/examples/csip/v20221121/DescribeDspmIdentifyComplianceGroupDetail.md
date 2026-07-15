**Example 1: DescribeDspmIdentifyComplianceGroupDetail**



Input: 

```
tccli csip DescribeDspmIdentifyComplianceGroupDetail --cli-unfold-argument  \
    --MemberId mem-12edwqad \
    --Id 10000
```

Output: 
```
{
    "Response": {
        "Description": "kyrie描述",
        "Detail": [],
        "Id": 10000,
        "LevelGroupId": 1,
        "LevelGroupName": "系统-高中低",
        "Name": "kyrie测试",
        "Status": 1,
        "Type": 1,
        "RequestId": "0d7bc400-94ee-4dbd-a3a5-e3238cd3dfa5"
    }
}
```

