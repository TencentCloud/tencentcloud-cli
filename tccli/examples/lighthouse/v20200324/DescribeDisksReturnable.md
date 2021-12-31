**Example 1: 查询磁盘是否可退还**



Input: 

```
tccli lighthouse DescribeDisksReturnable --cli-unfold-argument  \
    --DiskIds lhdisk-eobj8huv
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DiskReturnableSet": [
            {
                "DiskId": "lhdisk-5vmz00i3",
                "IsReturnable": true,
                "ReturnFailCode": 0,
                "ReturnFailMessage": ""
            }
        ],
        "RequestId": "3eec6c10-a8c7-41e4-b4ba-c84a5000211d"
    }
}
```

