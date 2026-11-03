**Example 1: DescribeLoginWhiteCustomListEDR**

查询异常登录自定义白名单列表

Input: 

```
tccli csip DescribeLoginWhiteCustomListEDR --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 260199983,
                "CreateTime": "2026-10-23 15:38:40",
                "EndTime": "",
                "ExcludeInstanceIDs": [],
                "ExcludeQUUIDS": [],
                "HostCount": 0,
                "Id": 3,
                "InstanceIDs": [],
                "Locations": "",
                "ModifyTime": "2026-10-23 15:38:40",
                "Places": [],
                "QUUIDS": [],
                "Remark": "",
                "Scope": 1,
                "SrcIp": "1.1.1.2",
                "StartTime": "",
                "TagItems": [],
                "Type": "Custom",
                "UserName": "place"
            }
        ],
        "TotalCount": 2,
        "RequestId": "51c542e6-5cde-4adf-8f01-4e21e027cf20"
    }
}
```

