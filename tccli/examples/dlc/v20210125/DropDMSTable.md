**Example 1: DMS元数据删除表**



Input: 

```
tccli dlc DropDMSTable --cli-unfold-argument  \
    --DbName abc \
    --Name abc \
    --DeleteData True \
    --EnvProps.Key abc \
    --EnvProps.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

