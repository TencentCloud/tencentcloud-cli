**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DropTable --cli-unfold-argument  \
    --Name test \
    --DbName bob_test3 \
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
        "RequestId": "0ac0549d-0a6e-4640-8957-6816b81bc85b"
    }
}
```

