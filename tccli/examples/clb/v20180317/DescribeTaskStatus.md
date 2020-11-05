**Example 1: Querying async task status**

This example shows you how to query whether an async task is successfully executed if the call to the forwarding rule creating API is returned successfully and the returned `RequestId` is `55c85074-3e7f-4c6d-864f-673660d4f8de`. The `Status` value of 0 in the response indicates that the task succeeded.

Input: 

```
tccli clb DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 55c85074-3e7f-4c6d-864f-673660d4f8de
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "917384bc-5b8d-4b68-a0bc-a58f815e8e3b"
    }
}
```

