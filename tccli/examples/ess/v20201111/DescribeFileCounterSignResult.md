**Example 1: 根据TaskId查询任务结果**

根据TaskId查询任务结果

Input: 

```
tccli ess DescribeFileCounterSignResult --cli-unfold-argument  \
    --Operator.UserId yDCpyUc*******************bsVny9l \
    --Agent.ProxyOrganizationId yUIdyeU*******************bsdf234l \
    --TaskId yDtwuU*******************FYPZ
```

Output: 
```
{
    "Response": {
        "ErrorDetail": "",
        "RequestId": "s1737011895277384406",
        "ResultFileId": "yDtwwUUckp7m1csmUuFhivskVdRNkoJ9",
        "Status": "FINISHED"
    }
}
```

