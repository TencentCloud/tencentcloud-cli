**Example 1: 查询主节点当前正在运行的线程**



Input: 

```
tccli mariadb DescribeProcessList --cli-unfold-argument  \
    --InstanceId tdsql-048udnfz \
    --NodeId 7b1f6e62b767
```

Output: 
```
{
    "Response": {
        "ProcessList": [
            {
                "Command": "Sleep",
                "Db": "mysql",
                "Host": "9.71.144.188:55615",
                "Id": 951069,
                "Info": "",
                "ProcessStartTime": "2025-06-24 11:27:26",
                "State": "",
                "Time": 30,
                "User": "root"
            }
        ],
        "RequestId": "d4eb7e99-b3e6-45d6-ae6f-7358c7511cad-013"
    }
}
```

