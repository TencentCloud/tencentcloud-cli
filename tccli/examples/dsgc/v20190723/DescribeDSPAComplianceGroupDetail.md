**Example 1: 获取模板详情信息**

获取模板详情信息

Input: 

```
tccli dsgc DescribeDSPAComplianceGroupDetail --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "Detail": {
            "Id": 5,
            "Name": "开发模板",
            "Description": "",
            "ComplianceGroupType": 2,
            "CreateTime": "2022-10-16 16:42:16",
            "ModifyTime": "2022-10-16 16:42:16",
            "LevelGroupId": 1,
            "LevelGroupName": "系统-高中低"
        }
    }
}
```

