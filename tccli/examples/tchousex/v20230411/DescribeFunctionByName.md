**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeFunctionByName --cli-unfold-argument  \
    --DbName test \
    --FuncName fuzzy_equals \
    --FuncType (double,double) returns boolean \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993
```

Output: 
```
{
    "Response": {
        "ClassName": "com.cloudera.impala.FuzzyEqualsUdf",
        "DbName": "test",
        "Description": "",
        "ExtParameters": null,
        "FuncName": "fuzzy_equals",
        "FuncType": "(DOUBLE, DOUBLE) RETURNS BOOLEAN",
        "RequestId": "8589a73c-b638-4261-a9ef-00f6e583460e",
        "ResourceIdentifiers": [
            {
                "ResourceType": "cos",
                "ResourceUri": "xfs://warehouse-vgh8kk6k-1305504398/user/hive/udf/hive-udf-samples-1.0.jar"
            }
        ]
    }
}
```

