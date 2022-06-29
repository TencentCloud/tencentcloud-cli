**Example 1: DMS元数据删除表**



Input: 

```
tccli dlc DropDMSTable --cli-unfold-argument  \
    --DbName db1 \
    --Name table1 \
    --DeleteData False \
    --EnvProps.Value xx \
    --EnvProps.Key xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

