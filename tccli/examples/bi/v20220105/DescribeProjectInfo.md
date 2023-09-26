**Example 1: 展示项目详情接口示例**

展示项目详情接口示例

Input: 

```
tccli bi DescribeProjectInfo --cli-unfold-argument  \
    --Id 43
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "27f87002-9ec9-42b3-a416-f2c656056a32",
        "Extra": "",
        "Data": {
            "Id": 464,
            "CorpId": "700000404475",
            "ColorCode": "#066EFF",
            "PageCount": 25,
            "MemberCount": 1,
            "Logo": null,
            "Mark": null,
            "Name": "测试推送鉴权",
            "Seed": "4TygneQkusljIJoo",
            "Source": null,
            "LastModifyName": null,
            "AuthList": null,
            "Apply": false,
            "CreatedUser": "700000404475",
            "CreatedAt": "2022-12-29 10:36:08",
            "UpdatedUser": "700000404475",
            "UpdatedAt": "2023-01-09 16:52:45",
            "IsExternalManage": false,
            "ManagePlatform": null
        }
    }
}
```

