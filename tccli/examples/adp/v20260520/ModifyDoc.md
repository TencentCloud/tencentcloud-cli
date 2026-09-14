**Example 1: 修改单个文档**

修改单个文档

Input: 

```
tccli adp ModifyDoc --cli-unfold-argument  \
    --DocId 2067623425823338880 \
    --Fields.Name 肺鱼rename111.txt \
    --KbId 2067622575842400832 \
    --UpdateMask.Paths Name
```

Output: 
```
{
    "Response": {
        "RequestId": "e4e631fb-298b-440b-8a55-4b08691a10a3"
    }
}
```

