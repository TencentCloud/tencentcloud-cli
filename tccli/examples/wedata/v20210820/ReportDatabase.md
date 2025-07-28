**Example 1: 上报database元数据**

上报database元数据

Input: 

```
tccli wedata ReportDatabase --cli-unfold-argument  \
    --DatasourceId 62112 \
    --DatabaseName default1 \
    --Description default112 \
    --CreateTime 1751611555000 \
    --ModifiedTime 1751611555000
```

Output: 
```
{
    "Response": {
        "Guid": "9vcvhXr3p3_4ZSGWhiwhOQ",
        "RequestId": "3801cdf5-41d7-4031-b330-04f73e1ddc22"
    }
}
```

