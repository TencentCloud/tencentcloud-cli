**Example 1: 查询项目详情**

查询项目详情

Input: 

```
tccli iotexplorer DescribeProject --cli-unfold-argument  \
    --ProjectId prj-4r2kajtp
```

Output: 
```
{
    "Response": {
        "Project": {
            "ProjectId": "prj-4r2kajtp",
            "ProjectName": "字符串Name",
            "ProjectDesc": "字符串Desc",
            "CreateTime": 1557459725,
            "UpdateTime": 1559743207,
            "ProductCount": 0,
            "NativeAppCount": 0,
            "WebAppCount": 0
        },
        "RequestId": "672626b5-dbcd-4b5c-a43c-f731e80164c4"
    }
}
```

