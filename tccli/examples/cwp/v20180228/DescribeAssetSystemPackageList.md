**Example 1: 获取资产管理系统安装包列表**

获取资产管理系统安装包列表

Input: 

```
tccli cwp DescribeAssetSystemPackageList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Packages": [
            {
                "Name": "abc",
                "Desc": "abc",
                "Version": "abc",
                "InstallTime": "abc",
                "Type": "abc",
                "MachineName": "abc",
                "MachineIp": "abc",
                "OsInfo": "abc",
                "UpdateTime": "abc",
                "FirstTime": "abc",
                "IsNew": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

