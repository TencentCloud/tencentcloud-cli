**Example 1: Querying the list of permission groups**



Input: 

```
tccli cfs DescribeCfsPGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "PGroupList": [
            {
                "PGroupId": "pgroup-12345",
                "Name": "test",
                "DescInfo": "test",
                "BindCfsNum": 0,
                "CDate": "2019-07-05 19:04:18"
            },
            {
                "PGroupId": "pgroup-67890",
                "Name": "test2",
                "DescInfo": "test2",
                "BindCfsNum": 0,
                "CDate": "2019-07-06 10:57:29"
            },
            {
                "PGroupId": "pgroup-54321",
                "Name": "Test",
                "DescInfo": "use for test",
                "BindCfsNum": 1,
                "CDate": "2019-07-03 16:06:38"
            },
            {
                "PGroupId": "pgroupbasic",
                "Name": "Default permission group",
                "DescInfo": "Default permission group",
                "BindCfsNum": 5,
                "CDate": "2019-06-21 17:30:05"
            }
        ]
    }
}
```

