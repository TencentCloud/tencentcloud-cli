**Example 1: 删除实例SQL限流任务**

删除实例SQL限流任务

Input: 

```
tccli dbbrain DeleteSqlFilters --cli-unfold-argument  \
    --Product mysql \
    --InstanceId cdb-hxuthiy6 \
    --FilterIds 1089146 \
    --SessionToken xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "24665720-8c93-11eb-bee6-e98cea0e6794"
    }
}
```

