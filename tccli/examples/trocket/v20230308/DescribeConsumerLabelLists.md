**Example 1: 批量查询消费组灰度标签列表成功**



Input: 

```
tccli trocket DescribeConsumerLabelLists --cli-unfold-argument  \
    --InstanceId rmq-1****jjdr \
    --Groups grp-123708
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Results": [
            {
                "Group": "grp-123708",
                "TotalCount": 1,
                "Labels": [
                    {
                        "Label": "de123708",
                        "State": "ACTIVE",
                        "UpdatedAt": 1789631354847
                    }
                ]
            }
        ],
        "RequestId": "72e88f60-568f-4934-bd08-44320ee10e4c"
    }
}
```

