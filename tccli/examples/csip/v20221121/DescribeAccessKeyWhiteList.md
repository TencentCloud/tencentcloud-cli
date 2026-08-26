**Example 1: 访问密钥告警记录列表**



Input: 

```
tccli csip DescribeAccessKeyWhiteList --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AKList": [
                    "AKIDZ***ABA4",
                    "AK***Va",
                    "AKI***k"
                ],
                "ActionList": [],
                "AkImportType": 0,
                "AppID": 1256299843,
                "CallType": 0,
                "CreateTime": "2025-02-27 20:01:23",
                "ErrorCodeList": [],
                "ID": 10000,
                "IPList": [],
                "Name": "test",
                "Nickname": "name",
                "Remark": "",
                "Uin": "10000450***",
                "UpdateTime": "2025-02-27 20:01:23"
            }
        ],
        "RequestId": "b8e179b8-1135-4e34-a69a-ecb4ba8a86b2",
        "Total": 1
    }
}
```

