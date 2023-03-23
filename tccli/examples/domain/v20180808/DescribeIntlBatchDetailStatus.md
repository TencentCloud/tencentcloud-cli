**Example 1: 查询批量详情状态**



Input: 

```
tccli domain DescribeIntlBatchDetailStatus --cli-unfold-argument  \
    --LogIds 12 13
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "Id": 12,
                "Status": "doing",
                "Reason": "",
                "ReasonZh": ""
            }
        ],
        "RequestId": "121323"
    }
}
```

