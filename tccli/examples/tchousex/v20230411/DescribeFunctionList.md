**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeFunctionList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993 \
    --DbName test
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "ClassName": "",
                "DbName": "test",
                "Description": "",
                "ExtParameters": null,
                "FuncName": "fuzzy_equals",
                "FuncType": "(DOUBLE, DOUBLE) RETURNS BOOLEAN",
                "ResourceIdentifiers": null
            }
        ],
        "RequestId": "e104156a-8abd-4058-a35c-b4d021b6200b",
        "TotalCount": 1
    }
}
```

