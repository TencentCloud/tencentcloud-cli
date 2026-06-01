**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex CreatePartition --cli-unfold-argument  \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value warehouse1 \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value 123456Abc \
    --Name d=4 \
    --DbName bob_test \
    --TableName test \
    --InstanceId warehouse-7fys4tj2
```

Output: 
```
{
    "Response": {
        "RequestId": "50ae43a8-3593-42f4-83c3-253fd6c25cbc"
    }
}
```

