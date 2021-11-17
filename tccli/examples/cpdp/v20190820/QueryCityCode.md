**Example 1: 查询城市编码接口成功示例**

查询城市编码接口成功

Input: 

```
tccli cpdp QueryCityCode --cli-unfold-argument  \
    --OpenId abc \
    --OpenKey 123
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "查询成功",
        "Result": [
            {
                "CityId": "110100",
                "Province": "北京",
                "City": "北京",
                "District": "东城区"
            }
        ]
    }
}
```

