**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DropFunction --cli-unfold-argument  \
    --DbName bob_test \
    --FuncName fuzzy_equals \
    --FuncType (double,double) returns boolean \
    --InstanceId warehouse-7fys4tj2 \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value warehouse1 \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value 123456Abc
```

Output: 
```
{
    "Response": {
        "RequestId": "0422a84f-df73-438e-a9cd-4856e0ea79b6"
    }
}
```

