**Example 1: 编辑空间**



Input: 

```
tccli adp ModifySpace --cli-unfold-argument  \
    --Name 编辑名称 \
    --Description 描述更改 \
    --SpaceId UYiGYydT \
    --FieldMask.Paths Name Description
```

Output: 
```
{
    "Response": {
        "RequestId": "2a7b25a8-59c1-4920-8881-c6199ab6d1c5"
    }
}
```

