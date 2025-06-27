**Example 1: 查看移动端资产**

查看移动端资产

Input: 

```
tccli ctem DescribeApps --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppVersion": "v1.1.1",
                "Description": "",
                "Developer": "tester",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 17:30:23",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "test",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "b5c10af2a904da1ce896da2800e4933b",
                    "UpdateAt": "2024-06-06 17:30:23"
                },
                "DownloadUrl": "http://a.test.com",
                "Id": 11,
                "Logo": "",
                "Name": "test",
                "PackageName": "com.test",
                "Platform": "android",
                "ServerUrl": "http://test.com"
            }
        ],
        "RequestId": "922257b7-c750-4d0c-8e74-3f4119551fee",
        "Total": 1
    }
}
```

