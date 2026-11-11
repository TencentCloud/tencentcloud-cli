**Example 1: DescribeModules**

查询当前实例开启module信息

Input: 

```
tccli redis DescribeModules --cli-unfold-argument  \
    --InstanceId crs-qkua****
```

Output: 
```
{
    "Response": {
        "Modules": [
            {
                "IsSupport": true,
                "Name": "Bloom",
                "Status": "OFF"
            },
            {
                "IsSupport": true,
                "Name": "JSON",
                "Status": "OFF"
            },
            {
                "IsSupport": false,
                "Name": "Search",
                "Status": "OFF"
            },
            {
                "IsSupport": false,
                "Name": "TimeSeries",
                "Status": "OFF"
            }
        ],
        "RequestId": "de51c573-17f9-40e8-9c0f-828ebd8a4346"
    }
}
```

