**Example 1: demo**



Input: 

```
tccli wedata DescribeCodeSearchAuditInfo --cli-unfold-argument  \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6b6d38ce-105a-4b5b-9392-1efa2544032e",
        "Data": {
            "CodeSearchAuditInfo": [
                {
                    "Id": 178,
                    "ProjectId": 1,
                    "Keyword": "hannah"
                },
                {
                    "Id": 177,
                    "ProjectId": 1,
                    "Keyword": "hive"
                },
                {
                    "Id": 176,
                    "ProjectId": 1,
                    "Keyword": "hive"
                },
                {
                    "Id": 175,
                    "ProjectId": 1,
                    "Keyword": "tsign_data"
                },
                {
                    "Id": 174,
                    "ProjectId": 1,
                    "Keyword": "tsign_data"
                }
            ]
        }
    }
}
```

**Example 2: demo1**



Input: 

```
tccli wedata DescribeCodeSearchAuditInfo --cli-unfold-argument  \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6b6d38ce-105a-4b5b-9392-1efa2544032e",
        "Data": {
            "CodeSearchAuditInfo": [
                {
                    "Id": 178,
                    "ProjectId": 1,
                    "Keyword": "hannah"
                },
                {
                    "Id": 177,
                    "ProjectId": 1,
                    "Keyword": "hive"
                },
                {
                    "Id": 176,
                    "ProjectId": 1,
                    "Keyword": "hive"
                },
                {
                    "Id": 175,
                    "ProjectId": 1,
                    "Keyword": "tsign_data"
                },
                {
                    "Id": 174,
                    "ProjectId": 1,
                    "Keyword": "tsign_data"
                }
            ]
        }
    }
}
```

