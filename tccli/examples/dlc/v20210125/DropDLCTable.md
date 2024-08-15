**Example 1: DLC元数据删除表**



Input: 

```
tccli dlc DropDLCTable --cli-unfold-argument  \
    --DbName database1 \
    --Name table1 \
    --DeleteData True \
    --DataEngineName engine1 \
    --ResourceGroupName group1
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

