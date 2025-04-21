**Example 1: 示例1**



Input: 

```
tccli ioa DescribeTableColumnSetting --cli-unfold-argument  \
    --TableId windows:/ioa/assetmanage/ngn/trustconfigure/business#check
```

Output: 
```
{
    "Response": {
        "RequestId": "78fb5123-bda3-40a8-a077-5d422335ab84",
        "Data": {
            "Items": [
                {
                    "TableId": "windows:/ioa/assetmanage/ngn/trustconfigure/business#check",
                    "Columns": [
                        "Name",
                        "IOAUserName",
                        "UserName",
                        "DeviceStrategyVer",
                        "SerialNum",
                        "NGNStrategyVer",
                        "generatorUnInstallCode",
                        "generatorPrerogativeCode",
                        "Ip",
                        "GroupName",
                        "Itime",
                        "DeviceMark",
                        "Tags",
                        "StrVersion",
                        "VulVersion"
                    ]
                }
            ]
        }
    }
}
```

