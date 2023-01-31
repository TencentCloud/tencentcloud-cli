**Example 1: 修改 RUM 应用信息**

修改 RUM 应用信息

Input: 

```
tccli rum ModifyProject --cli-unfold-argument  \
    --ID 6 \
    --Name '测试项目'
```

Output: 
```
{
    "Response": {
        "ID": 1,
        "Msg": "success",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

