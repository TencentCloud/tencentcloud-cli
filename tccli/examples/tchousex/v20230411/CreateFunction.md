**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex CreateFunction --cli-unfold-argument  \
    --DbName bob_test3 \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value warehouse1 \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value 123456Abc \
    --Description test \
    --FuncName fuzzy_equals \
    --FuncType (DOUBLE, DOUBLE) RETURNS BOOLEAN \
    --Resources.ResourceType cos \
    --Resources.ResourceUri xfs://warehouse-7fys4tj2-1305504398/user/hive/udf/hive-udf-samples-1.0.jar \
    --ClassName com.cloudera.impala.FuzzyEqualsUdf \
    --InstanceId warehouse-7fys4tj2
```

Output: 
```
{
    "Response": {
        "RequestId": "4fd708c3-7d9f-4e17-83cb-67270e6cbe48"
    }
}
```

