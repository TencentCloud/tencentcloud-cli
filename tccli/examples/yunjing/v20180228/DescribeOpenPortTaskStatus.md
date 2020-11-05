**Example 1: Getting the status of real-time port pulling task**

This example shows you how to get the status of a real-time port pulling task.

Input: 

```
tccli yunjing DescribeOpenPortTaskStatus --cli-unfold-argument  \
    --Uuid 6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1
```

Output: 
```
{
    "Response": {
        "Status": "COMPLETE",
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

