**Example 1: 删除指定库下的表**

删除demo库下的test表

Input: 

```
tccli cdwdoris DeleteTable --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --DbName demo \
    --TableName table1 \
    --IsForce False
```

Output: 
```
{
    "Response": {
        "Message": "message1",
        "RequestId": "41de726a-0bd6-4794-8324-5fd73c312886"
    }
}
```

