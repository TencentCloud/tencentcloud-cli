**Example 1: 成功示例**

调用接口成功

Input: 

```
tccli vdb DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId vdb-bmz0gqmd
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Name": "master-0",
                "Status": "Running"
            },
            {
                "Name": "search-0",
                "Status": "Running"
            },
            {
                "Name": "worker-0",
                "Status": "Running"
            },
            {
                "Name": "worker-1",
                "Status": "Pending"
            }
        ],
        "RequestId": "b3157916-a811-443f-af68-23220d6dfb01",
        "TotalCount": 5
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

