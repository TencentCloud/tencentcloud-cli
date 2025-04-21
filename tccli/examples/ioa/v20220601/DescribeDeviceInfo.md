**Example 1: 查询终端信息**



Input: 

```
tccli ioa DescribeDeviceInfo --cli-unfold-argument  \
    --Type process_list \
    --Mid 60A79588CD1400107221E490335AA1BA63730928
```

Output: 
```
{
    "Response": {
        "RequestId": "1c67af11-9c46-42aa-af5e-28f070199e82",
        "Data": {
            "NetworkList": null,
            "ServiceList": null,
            "ProcessList": null
        }
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa DescribeDeviceInfo --cli-unfold-argument  \
    --Mid EBCDB9C9923516F3C02B42B42DA564E7653F6EBC02 \
    --Type process_list
```

Output: 
```
{
    "Response": {
        "Data": {
            "NetworkList": null,
            "ProcessList": null,
            "ServiceList": null
        },
        "RequestId": "26a20612-155c-4de1-adcc-52358ff7fb36"
    }
}
```

