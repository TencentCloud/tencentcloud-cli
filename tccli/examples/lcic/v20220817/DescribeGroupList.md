**Example 1: 示例1**

TeacherId和MemberId都不填的返回结果

Input: 

```
tccli lcic DescribeGroupList --cli-unfold-argument  \
    --SdkAppId 3618809
```

Output: 
```
{
    "Response": {
        "GroupInfos": [
            {
                "GroupId": "cfmsqfu2r378uak93i70",
                "GroupName": "修改测试群组名称",
                "GroupType": 0,
                "SubGroupIds": null,
                "TeacherId": "2LoDvr6M9TvI4x4dMFBpGRzxZXr"
            },
            {
                "GroupId": "cfmst8u2r378uak93i90",
                "GroupName": "批量创建群组1",
                "GroupType": 0,
                "SubGroupIds": null,
                "TeacherId": ""
            },
            {
                "GroupId": "cfmst8u2r378uak93i9g",
                "GroupName": "批量创建群组2",
                "GroupType": 0,
                "SubGroupIds": null,
                "TeacherId": ""
            },
            {
                "GroupId": "cfmthke2r378uak93ii0",
                "GroupName": "测试修改群组",
                "GroupType": 0,
                "SubGroupIds": null,
                "TeacherId": "2LoDvr6M9TvI4x4dMFBpGRzxZXr"
            },
            {
                "GroupId": "cjdipop7qk6r714q0fh0",
                "GroupName": "lukatest",
                "GroupType": 0,
                "SubGroupIds": null,
                "TeacherId": ""
            }
        ],
        "RequestId": "5b261337-70dc-49a9-92cb-820641958626",
        "Total": 5
    }
}
```

**Example 2: 示例2**

查询TeacherId的结果

Input: 

```
tccli lcic DescribeGroupList --cli-unfold-argument  \
    --SdkAppId 3618809 \
    --TeacherId 2LoDvr6M9TvI4x4dMFBpGRzxZXr
```

Output: 
```
{
    "Response": {
        "GroupInfos": [
            {
                "GroupId": "cfmsqfu2r378uak93i70",
                "GroupName": "修改测试群组名称",
                "GroupType": 0,
                "SubGroupIds": null,
                "TeacherId": "2LoDvr6M9TvI4x4dMFBpGRzxZXr"
            },
            {
                "GroupId": "cfmthke2r378uak93ii0",
                "GroupName": "测试修改群组",
                "GroupType": 0,
                "SubGroupIds": null,
                "TeacherId": "2LoDvr6M9TvI4x4dMFBpGRzxZXr"
            }
        ],
        "RequestId": "a69c412e-1da6-4d27-bd37-c74a2703f94a",
        "Total": 2
    }
}
```

