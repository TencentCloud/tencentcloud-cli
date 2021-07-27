**Example 1: 查询实例的可设置参数列表**



Input: 

```
tccli sqlserver DescribeInstanceParams --cli-unfold-argument  \
    --InstanceId mssql-bm5e51kb
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CurrentValue": "24",
                "Default": "0",
                "Description": "The fill-factor option is provided for fine-tuning index data storage and performance.",
                "EnumValue": [],
                "Max": 100,
                "Min": 0,
                "Name": "fill factor(%)",
                "NeedReboot": 1,
                "ParamType": "integer",
                "Status": 0
            },
            {
                "CurrentValue": "0",
                "Default": "0",
                "Description": "The max worker threads option configures the number of worker threads that are available SQL Server-wide to process query requests, login, logout, and similar application requests.",
                "EnumValue": [
                    "0"
                ],
                "Max": 32767,
                "Min": 336,
                "Name": "max worker threads",
                "NeedReboot": 1,
                "ParamType": "integer",
                "Status": 0
            },
            {
                "CurrentValue": "30000",
                "Default": "5",
                "Description": "The cost threshold for parallelism option specifies the threshold at which SQL Server creates and runs parallel plans for queries.",
                "EnumValue": [],
                "Max": 32767,
                "Min": 0,
                "Name": "cost threshold for parallelism",
                "NeedReboot": 1,
                "ParamType": "integer",
                "Status": 0
            },
            {
                "CurrentValue": "1024",
                "Default": "0",
                "Description": "The degree of parallelism sets the number of processors employed to run a single statement, for each parallel plan execution. ",
                "EnumValue": [],
                "Max": 1024,
                "Min": 0,
                "Name": "max degree of parallelism",
                "NeedReboot": 1,
                "ParamType": "integer",
                "Status": 0
            },
            {
                "CurrentValue": "0",
                "Default": "0",
                "Description": "The optimize for ad hoc workloads option is used to improve the efficiency of the plan cache for workloads that contain many single use ad hoc batches.",
                "EnumValue": [
                    "0",
                    "1"
                ],
                "Max": 0,
                "Min": 0,
                "Name": "optimize for ad hoc workloads",
                "NeedReboot": 1,
                "ParamType": "enum",
                "Status": 0
            },
            {
                "CurrentValue": "1024",
                "Default": "0",
                "Description": "This options change the amount of memory the SQL Server Memory Manager can allocate to a SQL Server process.",
                "EnumValue": [],
                "Max": 2560,
                "Min": 0,
                "Name": "min server memory(MB)",
                "NeedReboot": 1,
                "ParamType": "integer",
                "Status": 0
            },
            {
                "CurrentValue": "23",
                "Default": "0",
                "Description": "Use the blocked process threshold option to specify the threshold, in seconds, at which blocked process reports are generated.",
                "EnumValue": [],
                "Max": 86400,
                "Min": 0,
                "Name": "blocked process threshold(s)",
                "NeedReboot": 1,
                "ParamType": "integer",
                "Status": 0
            }
        ],
        "RequestId": "8c2fa1ec-7e13-4a2b-ba20-4d5ef93047ad",
        "TotalCount": 7
    }
}
```

