**Example 1: 获取国家地区编码映射表**



Input: 

```
tccli gaap DescribeCountryAreaMapping --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "bdcb19c0-74db-47b1-a07c-bbe6985ef44c",
        "CountryAreaMappingList": [
            {
                "Remark": "1",
                "NationCountryName": "Fiji Islands",
                "GeographicalZoneInnerCode": "401000",
                "ContinentName": "Oceania",
                "ContinentInnerCode": "400000",
                "NationCountryInnerCode": "401012",
                "GeographicalZoneName": "Oceania"
            }
        ]
    }
}
```

