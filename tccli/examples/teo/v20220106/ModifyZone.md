**Example 1: 修改站点**



Input: 

```
tccli teo ModifyZone --cli-unfold-argument  \
    --VanityNameServers.Switch xx \
    --VanityNameServers.Servers xx \
    --Type xx \
    --Id xx
```

Output: 
```
{
    "Response": {
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
        "RequestId": "xx",
        "Type": "xx",
        "Id": "xx",
        "CnameStatus": "xx"
    }
}
```

