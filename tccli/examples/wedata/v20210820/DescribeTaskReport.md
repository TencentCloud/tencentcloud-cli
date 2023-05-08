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
        "TotalReadRecords": 2000000,
        "TotalReadBytes": 89898292,
        "TotalWriteRecords": 2000000,
        "TotalWriteBytes": 89898292,
        "TotalErrorRecords": 0,
        "RequestId": "xx"
    }
}
```

