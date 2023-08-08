**Example 1: 1**

1

Input: 

```
tccli wedata DescribeTaskByStatusReport --cli-unfold-argument  \
    --Type  \
    --TaskType  \
    --TypeName  \
    --ProjectId  \
    --StartTime  \
    --EndTime  \
    --AggregationUnit 
```

Output: 
```
{
    "Response": {
        "RequestId": "7198e47e-2532-4f81-9bfa-790451eb1723"
    }
}
```

**Example 2: 2**

2

Input: 

```
tccli wedata DescribeTaskByStatusReport --cli-unfold-argument  \
    --Type  \
    --TaskType  \
    --TypeName  \
    --ProjectId  \
    --StartTime  \
    --EndTime  \
    --AggregationUnit  \
    --CycleUnit  \
    --Status  \
    --InCharge 
```

Output: 
```
{
    "Response": {
        "RequestId": "fcbfd6fb-66a2-43be-bbe3-ab579806ff0e"
    }
}
```

