**Example 1: 获取企业全部审查要点清单**



Input: 

```
tccli ess DescribeEnterpriseContractReviewChecklists --cli-unfold-argument  \
    --Operator.UserId yDtUckphotltxpgD3IZBJ10dg
```

Output: 
```
{
    "Response": {
        "Checklists": [
            {
                "ConfigStatus": 1,
                "Count": 3,
                "Enabled": false,
                "Id": "yDtlUUckpfqe0eUx7RX5uRpuL96kx",
                "ModifiedOn": 1763628965,
                "Name": "审核",
                "Official": false,
                "Updater": "张三"
            },
            {
                "ConfigStatus": 1,
                "Count": 4,
                "Enabled": false,
                "Id": "yDtzUUkpfharbmUuErirRNRjLfwMQ",
                "ModifiedOn": 1763100881,
                "Name": "采购",
                "Official": false,
                "Updater": "李四"
            },
            {
                "ConfigStatus": 1,
                "Count": 4,
                "Enabled": true,
                "Id": "yDVUUckpfhvlrUuXEriCmkgEM2A6",
                "ModifiedOn": 1763091112,
                "Name": "购买",
                "Official": false,
                "Updater": "王五"
            }
        ],
        "RequestId": "f31368af-1ac2-47d6-80b6-146e12eb96eb",
        "Total": 3
    }
}
```

