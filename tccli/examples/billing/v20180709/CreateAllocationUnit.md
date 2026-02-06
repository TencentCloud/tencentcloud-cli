**Example 1: 创建分账目录树根结点**



Input: 

```
tccli billing CreateAllocationUnit --cli-unfold-argument  \
    --ParentId 0
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "ebe202d2-9746-4c9a-a931-f569651e5894"
    }
}
```

**Example 2: 创建普通分账单元**



Input: 

```
tccli billing CreateAllocationUnit --cli-unfold-argument  \
    --Name 财务部 \
    --ParentId 1
```

Output: 
```
{
    "Response": {
        "Id": 2,
        "RequestId": "5ac3b178-3434-452e-9a1e-dc8b8089a2d8"
    }
}
```

