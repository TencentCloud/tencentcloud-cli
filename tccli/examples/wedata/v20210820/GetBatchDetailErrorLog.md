**Example 1: 示例**



Input: 

```
tccli wedata GetBatchDetailErrorLog --cli-unfold-argument  \
    --JobId 1 \
    --ResourceId efc02db7-f631-458e-84e7-7947762eab8d \
    --ProjectId 1461767738399854592
```

Output: 
```
{
    "Response": {
        "Data": "delete workflow fail",
        "RequestId": "4b948422-9254-422c-9d0d-9c45935ca88c"
    }
}
```

**Example 2: 失败示例**



Input: 

```
tccli wedata GetBatchDetailErrorLog --cli-unfold-argument  \
    --JobId 2098 \
    --ResourceId 20240711234914005 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": "数据访问异常，当前任务可能已经删除，请刷新界面后重试，如果持续出现该问题，请联系客服",
        "RequestId": "d4d485ad-74a0-4e32-b21c-152f27651e2b"
    }
}
```

