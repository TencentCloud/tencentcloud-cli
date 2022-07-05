**Example 1: DMS元数据删除库**



Input: 

```
tccli dlc DropDMSDatabase --cli-unfold-argument  \
    --Name Name1 \
    --DeleteData False \
    --Cascade False
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

