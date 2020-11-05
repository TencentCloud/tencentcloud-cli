**Example 1: Querying usual login locations**

This example shows you how to query usual login locations.

Input: 

```
tccli yunjing DescribeUsualLoginPlaces --cli-unfold-argument ```

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

