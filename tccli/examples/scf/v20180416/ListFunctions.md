**Example 1: 获取函数列表**



Input: 

```
tccli scf ListFunctions --cli-unfold-argument  \
    --Limit 2 \
    --Order ASC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Functions": [
            {
                "Namespace": "defaut",
                "FunctionName": "functionName1",
                "FunctionId": "sdfdsgfd g",
                "Description": "",
                "Tags": [],
                "Runtime": "Nodejs8.9",
                "Type": "Event",
                "AsyncRunEnable": "FALSE",
                "TraceEnable": "FALSE",
                "ReservedConcurrencyMem": null,
                "TotalProvisionedConcurrencyMem": 0,
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": [],
                "AddTime": "2024-08-27 15:27:43",
                "ModTime": "2024-08-27 15:27:43"
            }
        ],
        "RequestId": "sdfsdfdg-7d05-4d3e-91f8-e62e6695c8c8"
    }
}
```

**Example 2: 根据标签查询函数**

查询status标签的值是dev，且owner标签的值是me的函数

Input: 

```
tccli scf ListFunctions --cli-unfold-argument  \
    --Filters.0.Name tag-status \
    --Filters.0.Values dev \
    --Filters.1.Name tag-owner \
    --Filters.1.Values me
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Functions": [
            {
                "Status": "Active",
                "FunctionName": "test",
                "TotalProvisionedConcurrencyMem": 1,
                "Namespace": "default",
                "Runtime": "Python3.6",
                "Type": "HTTP",
                "ReservedConcurrencyMem": 1,
                "Description": "just for test",
                "TraceEnable": "FALSE",
                "AsyncRunEnable": "FALSE",
                "FunctionId": "lam-xxxxxxxx",
                "StatusReasons": [],
                "StatusDesc": "",
                "AddTime": "2000-01-01 00:00:00",
                "ModTime": "2000-01-01 00:00:00",
                "Tags": [
                    {
                        "Value": "dev",
                        "Key": "status"
                    },
                    {
                        "Value": "me",
                        "Key": "owner"
                    }
                ]
            }
        ],
        "RequestId": "77ccef58-0ebb-4523-ab88-a37063443524"
    }
}
```

