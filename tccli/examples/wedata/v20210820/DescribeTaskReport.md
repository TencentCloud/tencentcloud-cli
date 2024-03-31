**Example 1: DescribeTaskReport**



Input: 

```
tccli wedata DescribeTaskReport --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 202205058668886 \
    --BeginDate 2022-05-01 \
    --EndDate 2022-05-05
```

Output: 
```
{
    "Response": {
        "TotalReadRecords": 1,
        "TotalReadBytes": 1,
        "TotalWriteRecords": 1,
        "TotalWriteBytes": 1,
        "TotalErrorRecords": 1,
        "RequestId": "abc"
    }
}
```

