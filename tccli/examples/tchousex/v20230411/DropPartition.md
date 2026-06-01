**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DropPartition --cli-unfold-argument  \
    --Name d=1,e=1 \
    --DbName bob_test \
    --TableName test1 \
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
        "RequestId": "5a20d589-dd39-4ce0-92b8-07ad90f54bbb"
    }
}
```

