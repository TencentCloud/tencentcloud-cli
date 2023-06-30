**Example 1: 示例**

扩容磁盘

Input: 

```
tccli cdwch ResizeDisk --cli-unfold-argument  \
    --InstanceId cdwch-adsfaas \
    --Type DATA \
    --DiskSize 300
```

Output: 
```
{
    "Response": {
        "InstanceId": "cdwch-adsfaas",
        "FlowId": "121",
        "RequestId": "asdfasdf-8jqwelasd-123aexdr",
        "ErrorMsg": ""
    }
}
```

