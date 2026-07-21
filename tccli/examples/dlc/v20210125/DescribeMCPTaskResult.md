**Example 1: MCP任务结果信息**



Input: 

```
tccli dlc DescribeMCPTaskResult --cli-unfold-argument  \
    --TaskId **************
```

Output: 
```
{
    "Response": {
        "TaskResult": {
            "CanDownload": false,
            "DisplayFormat": "",
            "IsResultOversize": false,
            "NextToken": "",
            "OutputMessage": "**** result ***** completed",
            "QueryResultTime": 0,
            "ResultSchema": [
                {
                    "Comment": "",
                    "CreateTime": "",
                    "DataMaskStrategyInfo": null,
                    "IsPartition": false,
                    "ModifiedTime": "",
                    "Name": "col1",
                    "Nullable": "",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "string"
                }
            ],
            "ResultSet": "[[\"value1\"],[\"value2\"]]",
            "RowAffectInfo": "2",
            "State": 2,
            "TaskId": "11jd01j-12f9h1"
        },
        "RequestId": "1aa1dc9a-adaf-4b05-a2ea-76ecc0d7ea08"
    }
}
```

