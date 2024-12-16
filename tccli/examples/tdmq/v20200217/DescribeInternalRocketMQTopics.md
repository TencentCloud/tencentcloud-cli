**Example 1: 查询主题列表**

查询主题列表

Input: 

```
tccli tdmq DescribeInternalRocketMQTopics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Topics": [
            {
                "Name": "xx",
                "Type": "xx",
                "GroupNum": 1,
                "Remark": "xx",
                "PartitionNum": 1,
                "CreateTime": 1,
                "UpdateTime": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

