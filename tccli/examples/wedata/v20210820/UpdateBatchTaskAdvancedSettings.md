**Example 1: 失败**

失败

Input: 

```
tccli wedata UpdateBatchTaskAdvancedSettings --cli-unfold-argument  \
    --TaskIds abc \
    --RetryWait 0 \
    --TryLimit 0 \
    --RunPriority 0 \
    --ExecutionTTL 0 \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 失败2**

失败2

Input: 

```
tccli wedata UpdateBatchTaskAdvancedSettings --cli-unfold-argument  \
    --TaskIds 20230608210301228 \
    --RetryWait 6 \
    --TryLimit 6 \
    --RunPriority 6 \
    --ExecutionTTL -1 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "Connect to 30.181.47.157:49222 [/30.181.47.157] failed: Connection refused (Connection refused) executing POST http://platformgateway/cloudapi/platformgateway/v1/platform/DescribeUserName"
        },
        "RequestId": "531163be-73d7-444f-b063-fba735e22fef"
    }
}
```

**Example 3: 成功**



Input: 

```
tccli wedata UpdateBatchTaskAdvancedSettings --cli-unfold-argument  \
    --TaskIds abc \
    --RetryWait 0 \
    --TryLimit 0 \
    --RunPriority 0 \
    --ExecutionTTL 0 \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 4: 成功2**

成功2

Input: 

```
tccli wedata UpdateBatchTaskAdvancedSettings --cli-unfold-argument  \
    --TaskIds 20230804121936196 \
    --RetryWait 7 \
    --TryLimit 7 \
    --RunPriority 5 \
    --ExecutionTTL 7 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

