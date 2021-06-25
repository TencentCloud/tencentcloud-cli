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
        "RequestId": "24665720-8c93-11eb-bee6-e98cea0e6794",
        "ProcessList": [
            {
                "Host": "127.0.0.1:42036",
                "State": "",
                "Command": "Sleep",
                "Time": "1179",
                "ID": "171588317",
                "User": "root",
                "Info": "",
                "DB": "test"
            }
        ]
    }
}
```

