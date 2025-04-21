**Example 1: 按终端查看软件统计**



Input: 

```
tccli ioa DescribeSoftCensusListByDevice --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "UserName": "abc",
                    "MacAddr": "abc",
                    "Name": "abc",
                    "GroupNamePath": "abc",
                    "Ip": "abc",
                    "Mid": "abc",
                    "IoaUserName": "abc",
                    "GroupId": 0,
                    "GroupName": "abc",
                    "Id": 0,
                    "SoftNum": 0,
                    "PiracyRisk": 0
                }
            ],
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            }
        },
        "RequestId": "abc"
    }
}
```

