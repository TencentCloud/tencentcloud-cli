**Example 1: 查询用户站点信息列表**



Input: 

```
tccli teo DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Zones": [
            {
                "Status": "xx",
                "ModifiedOn": "2020-09-22T00:00:00+00:00",
                "Name": "xx",
                "NameServers": [
                    "xx"
                ],
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "OriginalNameServers": [
                    "xx"
                ],
                "Paused": true,
                "Type": "xx",
                "Id": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

