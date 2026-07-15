**Example 1: DescribeVariableList**

查询变量列表

Input: 

```
tccli adp DescribeVariableList --cli-unfold-argument  \
    --AppId 206*************184 \
    --ModuleType 1 \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "VariableList": [
            {
                "DefaultFileName": "",
                "DefaultValue": "2",
                "Description": "dd",
                "ModuleType": 1,
                "Name": "mmd",
                "Type": 1,
                "VariableId": "9cd*****************e*b-2e2fdaf67d5f"
            }
        ],
        "RequestId": "92e55ece-d96d-41aa-b5cb-a8256174912a"
    }
}
```

