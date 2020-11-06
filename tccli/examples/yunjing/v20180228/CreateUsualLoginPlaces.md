**Example 1: Adding usual login location**

This example shows you how to add a usual login location.

Input: 

```
tccli yunjing CreateUsualLoginPlaces --cli-unfold-argument  \
    --Uuid add4a78a-0d59-11e8-b7ab-00e081e1a5c5 \
    --Areas.0.CityId 1 \
    --Areas.0.ProvinceId 1 \
    --Areas.0.CountryId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

