**Example 1: 查询常用登录地**

查询常用登录地

Input: 

```
tccli cwp DescribeUsualLoginPlaces --cli-unfold-argument  \
    --Uuid add4a78a-0d59-11e8-b7ab-00e081e1a5c5
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "UsualLoginPlaces": [
            {
                "Id": 1,
                "Uuid": "add4a78a-0d59-11e8-b7ab-00e081e1a5c5",
                "CountryId": 1,
                "ProvinceId": 1,
                "CityId": 1
            }
        ]
    }
}
```

