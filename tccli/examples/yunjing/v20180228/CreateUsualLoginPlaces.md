**Example 1: 添加常用登录地**

添加常用登录地

Input: 

```
tccli yunjing CreateUsualLoginPlaces --cli-unfold-argument  \
    --Uuids add4a78a-0d59-11e8-b7ab-00e081e1a5c5 \
    --Places.0.CityId 1 \
    --Places.0.ProvinceId 1 \
    --Places.0.CountryId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

