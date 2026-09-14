**Example 1: 查询知识库列表**

查询知识库列表

Input: 

```
tccli adp DescribeKBSummaryList --cli-unfold-argument  \
    --SpaceId default_space \
    --PageNumber 1 \
    --PageSize 100 \
    --Query 共享知识库_文档问答PG检索开_adp_qta_ZRWBJY
```

Output: 
```
{
    "Response": {
        "KbList": [],
        "TotalCount": 0,
        "RequestId": "c03c9513-4994-4feb-8f44-d89efaaef369"
    }
}
```

