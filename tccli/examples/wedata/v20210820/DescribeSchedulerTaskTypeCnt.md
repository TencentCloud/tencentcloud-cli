**Example 1: 示例一**

示例一

Input: 

```
tccli wedata DescribeSchedulerTaskTypeCnt --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Number": "26",
                "TaskType": "35",
                "TypeName": "Shell"
            },
            {
                "Number": "5",
                "TaskType": "34",
                "TypeName": "Hive SQL"
            },
            {
                "Number": "1",
                "TaskType": "30",
                "TypeName": "Python"
            }
        ],
        "RequestId": "5a95de10-2d07-4c4b-ad03-fcc8e1c5c1f7"
    }
}
```

**Example 2: 1**

1

Input: 

```
tccli wedata DescribeSchedulerTaskTypeCnt --cli-unfold-argument  \
    --ProjectId 1 \
    --InCharge 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnknownParameter",
            "Message": "The parameter `InCharge` is not recognized."
        },
        "RequestId": "11beba5a-ce1f-4347-a64e-29e60cb9955d"
    }
}
```

