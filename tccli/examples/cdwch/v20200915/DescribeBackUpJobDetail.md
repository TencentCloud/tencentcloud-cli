**Example 1: 示例**



Input: 

```
tccli cdwch DescribeBackUpJobDetail --cli-unfold-argument  \
    --InstanceId xx \
    --BackUpJobId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TableContents": [
            {
                "Table": "xx",
                "Ips": "xx",
                "VCluster": "xx",
                "TotalBytes": 0,
                "Database": "xx"
            }
        ]
    }
}
```

