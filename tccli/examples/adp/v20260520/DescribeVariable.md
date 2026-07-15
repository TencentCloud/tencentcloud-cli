**Example 1: DescribeVariable**

查询环境变量

Input: 

```
tccli adp DescribeVariable --cli-unfold-argument  \
    --AppId 2060*************84 \
    --VariableId 9cdbf948-4d12-440a-8eeb-2e2fdaf67d5f \
    --ModuleType 1
```

Output: 
```
{
    "Response": {
        "Variable": {
            "DefaultFileName": "",
            "DefaultValue": "2",
            "Description": "dd",
            "ModuleType": 1,
            "Name": "mmd",
            "Type": 1,
            "VariableId": "9cdb***********************fdaf67d5f"
        },
        "RequestId": "6c04de0b-cf0e-43af-b850-4015ca115890"
    }
}
```

