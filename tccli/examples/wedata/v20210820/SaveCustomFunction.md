**Example 1: 保存用户自定义函数**



Input: 

```
tccli wedata SaveCustomFunction --cli-unfold-argument  \
    --Kind ANALYSIS \
    --Description test \
    --ReturnDesc test \
    --ParamDesc test \
    --Example  \
    --ClassName com.test.Ad \
    --Usage UDFRepeat(var,2) \
    --ResourceList.0.Path /1219-agent-1ertty559/datastudio/not_del_for_auto/udf-demo-1.0-SNAPSHOT.jar \
    --ResourceList.0.Id b0d9f61f-d15f-4723-8e06-9218b3fd57b3 \
    --ResourceList.0.Type cos \
    --ResourceList.0.Name udf-demo-1.0-SNAPSHOT.jar \
    --ResourceList.0.Md5  \
    --ClusterIdentifier hive-emr-tegfgd \
    --FunctionId d65df5af-28b4-4171-9a24-ce96fc4e83fa
```

Output: 
```
{
    "Response": {
        "ErrorMessage": null,
        "FunctionId": "d65df5af-28b4-4171-9a24-ce96fc4e83fa",
        "RequestId": "ef431542-96ae-467c-b821-f594df8ac83c"
    }
}
```

