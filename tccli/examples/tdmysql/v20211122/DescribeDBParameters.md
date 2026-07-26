**Example 1: 获取数据库当前参数**



Input: 

```
tccli tdmysql DescribeDBParameters --cli-unfold-argument  \
    --InstanceId tdsql3-ige1a5k3
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql3-ige1a5k3",
        "Params": [
            {
                "Default": "1",
                "SetValue": "",
                "Value": "1",
                "Param": "auto_increment_increment",
                "Constraint": {
                    "Range": {
                        "Max": "65535",
                        "Min": "1"
                    },
                    "Type": "section"
                },
                "HaveSetValue": false,
                "NeedRestart": true,
                "Description": ""
            },
            {
                "Default": "ON",
                "SetValue": "",
                "Description": "",
                "Value": "ON",
                "Param": "autocommit",
                "Constraint": {
                    "Enum": "ON,OFF",
                    "Type": "enum"
                },
                "HaveSetValue": false,
                "NeedRestart": true
            }
        ],
        "RequestId": "914db412-d6e6-47ad-8e62-d06e02e52a56"
    }
}
```

