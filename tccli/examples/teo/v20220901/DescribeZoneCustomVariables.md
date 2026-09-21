**Example 1: 查询站点级自定义变量配置**

查询站点 zone-3t7hlhw8*6o* 的站点级自定义变量配置。

Input: 

```
tccli teo DescribeZoneCustomVariables --cli-unfold-argument  \
    --ZoneId zone-3t7hlhw8*6o*
```

Output: 
```
{
    "Response": {
        "CustomVariableOperations": [],
        "CustomVariables": [
            {
                "Description": "",
                "InitialValue": "124",
                "Name": "user.zone.test2"
            }
        ],
        "RequestId": "dfaf688e-86f6-4b0d-8b76-ba6aa5b3d7bf"
    }
}
```

