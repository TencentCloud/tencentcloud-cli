**Example 1: DescribeMySQLTaskStatus**



Input: 

```
tccli tcb DescribeMySQLTaskStatus --cli-unfold-argument  \
    --EnvId *******pre-******bc0df14561 \
    --TaskId 16710 \
    --TaskName DeleteDataHub
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": "SUCCESS",
            "StatusDesc": ""
        },
        "RequestId": "85002631-5ed1-4e27-974a-7a5ffcd5fbae"
    }
}
```

