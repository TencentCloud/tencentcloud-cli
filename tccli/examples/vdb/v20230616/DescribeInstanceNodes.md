**Example 1: 成功示例**

调用接口成功

Input: 

```
tccli vdb DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId vdb-ecbgiqwb
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Name": "master-0"
            },
            {
                "Name": "search-0"
            },
            {
                "Name": "worker-0"
            }
        ],
        "RequestId": "c0c57557-d604-4bfc-abed-5ae659961720",
        "TotalCount": 3
    }
}
```

**Example 2: 调用失败**

调用接口失败

Input: 

```
tccli vdb DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId vdb-ecbgiqwb1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "instance \"vdb-ecbgiqwb1\" not found"
        },
        "RequestId": "e74de2e6-6f46-4cc3-b77a-15d799fedde9"
    }
}
```

