**Example 1: 查询IP状态接口示例**

查询IP状态接口

Input: 

```
tccli cfw DescribeIPStatusList --cli-unfold-argument  \
    --IPList 124.220.226.180
```

Output: 
```
{
    "Response": {
        "RequestId": "3fc3d1f9-b80f-4c2b-88c9-e3a8c0ec5ddd",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "StatusList": [
            {
                "IP": "124.220.226.180",
                "Status": 1
            }
        ]
    }
}
```

