**Example 1: 获取数据库当前参数**



Input: 

```
tccli mariadb DescribeDBParameters --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql-ige1a5k3",
        "Params": [
            {
                "Default": "1",
                "SetValue": "",
                "Value": "1",
                "Param": "auto_increment_increment",
                "HaveSetValue": false,
                "NeedRestart": false,
                "Constraint": {
                    "String": "",
                    "Enum": "",
                    "Range": {
                        "Max": "65535",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            }
        ],
        "RequestId": "914db412-d6e6-47ad-8e62-d06e02e52a56"
    }
}
```

