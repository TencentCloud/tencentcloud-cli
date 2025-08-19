**Example 1: 测试查询**

测试查询

Input: 

```
tccli ioa DescribeSoftwareInformation --cli-unfold-argument  \
    --Mid 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "Page": {
                "PageCount": 0,
                "PageNum": 1,
                "PageSize": 1000,
                "Total": 0
            }
        },
        "RequestId": "6b01b324-c25a-4297-8fb7-28401163f04a"
    }
}
```

