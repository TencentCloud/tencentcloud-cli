**Example 1: 查询任务状态**

根据任务id查询任务状态

Input: 

```
tccli cxm DescribeTask --cli-unfold-argument  \
    --FlowId 991304405
```

Output: 
```
{
    "Response": {
        "Status": "RUNNING",
        "RequestId": "ea165702-5042-4d64-8e76-aba1f163e337"
    }
}
```

