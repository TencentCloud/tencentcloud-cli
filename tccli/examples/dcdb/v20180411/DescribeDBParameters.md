**Example 1: 获取数据库当前参数**



Input: 

```
tccli dcdb DescribeDBParameters --cli-unfold-argument  \
    --InstanceId dcdbt-ige1a5k3
```

Output: 
```
{
    "Response": {
        "InstanceId": "dcdbt-ige1a5k3",
        "Params": [
            {
                "Default": "1",
                "SetValue": "",
                "Value": "1",
                "Param": "auto_increment_increment",
                "HaveSetValue": false,
                "NeedRestart": false,
                "Constraint": {
                    "Enum": "",
                    "String": "",
                    "Range": {
                        "Max": "65535",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            }
        ],
        "RequestId": "affa5c39-02b7-482a-a16f-a74e660e7b7f"
    }
}
```

