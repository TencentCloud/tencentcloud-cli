**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex CreateTable --cli-unfold-argument  \
    --Columns.0.Description a \
    --Columns.0.Type INT \
    --Columns.0.Name a \
    --Columns.1.Description b \
    --Columns.1.Length 10 \
    --Columns.1.Type VARCHAR \
    --Columns.1.Name b \
    --Columns.2.Description c \
    --Columns.2.Precision 10 \
    --Columns.2.Scale 3 \
    --Columns.2.Type Decimal \
    --Columns.2.Name c \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value warehouse1 \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value 123456Abc \
    --Description test table \
    --InstanceId warehouse-7fys4tj2 \
    --Name test \
    --DbName bob_test3 \
    --Type table \
    --Partitions.0.Type INT \
    --Partitions.0.Name d \
    --Partitions.1.Type INT \
    --Partitions.1.Name e
```

Output: 
```
{
    "Response": {
        "RequestId": "1d723061-de43-423d-b29a-dbcc587ce118"
    }
}
```

**Example 2: 测试示例2**

测试示例2

Input: 

```
tccli tchousex CreateTable --cli-unfold-argument  \
    --Columns.0.Name id \
    --Columns.1.Name name \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993 \
    --InstanceId warehouse-vgh8kk6k \
    --Name v3 \
    --DbName test \
    --SQL select id,name from t5 \
    --Type view
```

Output: 
```
{
    "Response": {
        "RequestId": "e6f4a279-de5b-49e9-aff6-6047dc2ba850"
    }
}
```

