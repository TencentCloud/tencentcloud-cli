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
                "ModTime": "xx",
                "Status": "xx",
                "StatusDesc": "xx",
                "FunctionName": "xx",
                "TotalProvisionedConcurrencyMem": 1,
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "AddTime": "xx",
                "Namespace": "xx",
                "StatusReasons": [
                    {
                        "ErrorCode": "xx",
                        "ErrorMessage": "xx"
                    }
                ],
                "Runtime": "xx",
                "Type": "xx",
                "FunctionId": "xx",
                "ReservedConcurrencyMem": 1,
                "Description": "xx",
                "TraceEnable": "FALSE",
                "AsyncRunEnable": "FALSE"
            }
        ],
        "RequestId": "xx"
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
                "ModTime": "xx",
                "Status": "xx",
                "StatusDesc": "xx",
                "FunctionName": "xx",
                "TotalProvisionedConcurrencyMem": 1,
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "AddTime": "xx",
                "Namespace": "xx",
                "StatusReasons": [
                    {
                        "ErrorCode": "xx",
                        "ErrorMessage": "xx"
                    }
                ],
                "Runtime": "xx",
                "Type": "xx",
                "FunctionId": "xx",
                "ReservedConcurrencyMem": 1,
                "Description": "xx",
                "TraceEnable": "FALSE",
                "AsyncRunEnable": "FALSE"
            }
        ],
        "RequestId": "xx"
    }
}
```

