**Example 1: 查询实时线程列表。**



Input: 

```
tccli dbbrain DescribeMySqlProcessList --cli-unfold-argument  \
    --Product mysql \
    --InstanceId cdb-test \
    --User root
```

Output: 
```
{
    "Response": {
        "ProcessList": [
            {
                "Command": "Query",
                "DB": "",
                "Host": "100.98.212.252:29285",
                "ID": "2075425",
                "Info": "/* p = 2342 , f=abd */  select sleep(1000)",
                "State": "User sleep",
                "Time": "103",
                "User": "root"
            }
        ],
        "RequestId": "7d0d84f2-d4c0-4349-b5a3-cd70b6efbdfe",
        "Statistics": [
            {
                "Data": [
                    {
                        "Count": 1,
                        "Name": "f=abd,p=2342",
                        "TimeAvg": 103,
                        "TimeSum": 103
                    }
                ],
                "Dimension": "SqlTag"
            }
        ]
    }
}
```

