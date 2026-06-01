**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex ModifyTable --cli-unfold-argument  \
    --Columns.0.Description a \
    --Columns.0.Type INT \
    --Columns.0.Name a \
    --Columns.1.Description b \
    --Columns.1.Length 20 \
    --Columns.1.Type CHAR \
    --Columns.1.Name b \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value warehouse1 \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value 123456Abc \
    --Description test2 \
    --InstanceId warehouse-7fys4tj2 \
    --Name test2 \
    --DbName bob_test
```

Output: 
```
{
    "Response": {
        "RequestId": "54f18f7e-28bc-4c58-923d-799d9a45b986"
    }
}
```

