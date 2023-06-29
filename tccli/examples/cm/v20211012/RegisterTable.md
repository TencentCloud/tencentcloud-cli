**Example 1: 预注册表结构**

预注册表结构

Input: 

```
tccli cm RegisterTable --cli-unfold-argument  \
    --Namespace nandy_ns \
    --Measurement Measurement \
    --Fields.0.Values tag \
    --Fields.0.Name tag1 \
    --Fields.1.Values sum \
    --Fields.1.Name field1 \
    --Fields.2.Values histogram@count histogram@+Inf histogram@1000_0000 \
    --Fields.2.Name field2 \
    --Type mc
```

Output: 
```
{
    "Response": {
        "Msg": "Success.",
        "RequestId": "xxx"
    }
}
```

