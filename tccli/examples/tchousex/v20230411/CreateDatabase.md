**Example 1: 测试用例**

测试用例

Input: 

```
tccli tchousex CreateDatabase --cli-unfold-argument  \
    --Description test \
    --InstanceId warehouse-7fys4tj2 \
    --Name bob_test3 \
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
        "RequestId": "e24ef618-94f0-4e61-9c7b-ef04c81fd924"
    }
}
```

