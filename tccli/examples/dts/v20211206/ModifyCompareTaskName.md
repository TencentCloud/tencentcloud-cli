**Example 1: 修改一致性校验任务名称**



Input: 

```
tccli dts ModifyCompareTaskName --cli-unfold-argument  \
    --JobId dts-p1sposne \
    --TaskName test_cmp \
    --CompareTaskId dts-p1sposne-cmp-37skmii9
```

Output: 
```
{
    "Response": {
        "RequestId": "ac300ff0-00f2-11ed-b005-4930e69d89c2"
    }
}
```

