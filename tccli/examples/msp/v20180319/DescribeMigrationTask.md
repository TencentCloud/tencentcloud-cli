**Example 1: Obtaining the specified migration task details**

This example shows you how to obtain the specified migration task details.

Input: 

```
tccli msp DescribeMigrationTask --cli-unfold-argument  \
    --TaskId msp-1vogxxxx
```

Output: 
```
{
    "Response": {
        "TaskStatus": [
            {
                "Status": "unstart",
                "Progress": "-",
                "UpdateTime": "2018-07-16 17:27:45"
            },
            {
                "Status": "migrating",
                "Progress": "-",
                "UpdateTime": "2018-07-16 17:27:45"
            },
            {
                "Status": "finish",
                "Progress": "-",
                "UpdateTime": "2018-07-16 17:40:51"
            }
        ],
        "RequestId": "ca59d091-0d07-4516-8375-dd88db394b81"
    }
}
```

