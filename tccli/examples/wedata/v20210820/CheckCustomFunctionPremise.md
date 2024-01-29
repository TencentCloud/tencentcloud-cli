**Example 1: 新建用户自定义函数组件检查**



Input: 

```
tccli wedata CheckCustomFunctionPremise --cli-unfold-argument  \
    --ClusterIdentifier hive_emr-dbcygrxq \
    --Type SPARK
```

Output: 
```
{
    "Response": {
        "LivyInstalled": true,
        "ErrorMessage": "相应组件不存在",
        "SparkInstalled": true,
        "RequestId": "d21f43aa-96a8-40a6-92b1-59f09b36f640"
    }
}
```

