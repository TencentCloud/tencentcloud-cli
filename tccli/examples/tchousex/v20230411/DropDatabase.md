**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DropDatabase --cli-unfold-argument  \
    --Cascade True \
    --Name bob_test3 \
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
        "RequestId": "c78e3b69-8435-42ad-83ef-5d6cd4788385"
    }
}
```

